import json
import logging
import os
import re
from datetime import datetime

import pandas as pd
from django.conf import settings
from django.http import FileResponse, Http404
from django.shortcuts import render

from .forms import UploadFileForm


LOGGER = logging.getLogger(__name__)
PANDAS_DUPLICATE_SUFFIX = re.compile(r"\.\d+$")
REQUEST_ID_KEYS = {"requestid"}
FIXED_KEYS = {
    "objectid",
    "objecttype",
    "userid",
    "requestid",
    "method",
    "path",
    "value",
}
EXCLUDED_KEYS = {"name"}
DEFAULT_BATCH_REQUEST = {
    "batch_request_id": "update test1",
    "batch_update_url": "https://client-api-domain.com/batch_status_update/",
}


def _strip_duplicate_suffix(column_name):
    return PANDAS_DUPLICATE_SUFFIX.sub("", str(column_name).strip())


def _normalize_key(column_name):
    base_name = _strip_duplicate_suffix(column_name)
    return re.sub(r"[\s_]+", "", base_name).lower()


def _is_meta_field(column_name):
    return _normalize_key(column_name).startswith("metafields.")


def _meta_field_name(column_name):
    base_name = _strip_duplicate_suffix(column_name)
    if "." not in base_name:
        return ""
    return base_name.split(".", 1)[1].strip()


def _get_metafield_columns(df_columns):
    """
    Identifies metafield columns by finding the 'metaFields' marker column,
    then collecting all columns after it until a fixed key is encountered.
    """
    df_columns_list = list(df_columns)
    metafield_marker_idx = None
    
    # Find the metaFields marker column
    for idx, col in enumerate(df_columns_list):
        if _normalize_key(col) == "metafields":
            metafield_marker_idx = idx
            break
    
    if metafield_marker_idx is None:
        return []
    
    # Collect columns after metaFields marker until we hit a fixed key
    metafield_cols = []
    for idx in range(metafield_marker_idx + 1, len(df_columns_list)):
        col = df_columns_list[idx]
        # Check if this column is a fixed key (stop collecting)
        if _normalize_key(col) in FIXED_KEYS:
            break
        metafield_cols.append(col)
    
    return metafield_cols


def _cell_has_value(value):
    return pd.notna(value) and str(value).strip() != ""


def _stringify_value(value):
    if isinstance(value, (pd.Timestamp, datetime)):
        return value.strftime("%Y-%m-%d")
    return str(value).strip()


def _get_first_value(row, columns):
    for column in columns:
        value = row.get(column)
        if _cell_has_value(value):
            return _stringify_value(value)
    return None


def _build_body(row, df_columns):
    body = {}

    object_id_columns = [col for col in df_columns if _normalize_key(col) == "objectid"]
    legacy_object_id_columns = [col for col in df_columns if str(_strip_duplicate_suffix(col)).strip() == "object_id"]
    user_id_columns = [col for col in df_columns if _normalize_key(col) == "userid"]
    object_type_columns = [col for col in df_columns if _normalize_key(col) == "objecttype"]

    legacy_object_id = _get_first_value(row, legacy_object_id_columns)
    object_id = _get_first_value(row, object_id_columns)
    user_id = _get_first_value(row, user_id_columns)

    if legacy_object_id:
        body["object_id"] = legacy_object_id
        body["object_type"] = "Reports"
    elif object_id:
        body["objectId"] = object_id
        body["objectType"] = _get_first_value(row, object_type_columns) or "Transaction"
    elif user_id:
        body["userId"] = user_id
    else:
        return None

    # Get metafield columns using new position-based detection
    metafield_cols = _get_metafield_columns(df_columns)

    for column in df_columns:
        normalized_key = _normalize_key(column)
        
        # Skip fixed keys, excluded keys, metaFields marker, and metafield columns
        if (normalized_key in FIXED_KEYS or 
            normalized_key in EXCLUDED_KEYS or 
            normalized_key == "metafields" or
            column in metafield_cols or
            _is_meta_field(column)):
            continue

        value = row.get(column)
        if not _cell_has_value(value):
            continue

        body[_strip_duplicate_suffix(column)] = _stringify_value(value)

    # Handle both old format (metaFields.x) and new format (columns after metaFields marker)
    meta_fields = {}
    
    # Old format: metaFields.fieldName columns
    for column in df_columns:
        if not _is_meta_field(column):
            continue

        value = row.get(column)
        if not _cell_has_value(value):
            continue

        meta_key = _meta_field_name(column)
        if meta_key:
            meta_fields[meta_key] = _stringify_value(value)
    
    # New format: columns between metaFields marker and next fixed key
    # Skip columns that are already in old format (starting with metaFields.) to avoid duplicates
    for column in metafield_cols:
        # Skip if this is an old format column (already processed above)
        if _is_meta_field(column):
            continue
            
        value = row.get(column)
        if not _cell_has_value(value):
            continue
        
        # Use the column name as-is for the metafield name
        meta_fields[_strip_duplicate_suffix(column)] = _stringify_value(value)

    if meta_fields:
        body["metaFields"] = meta_fields

    request_id_columns = [col for col in df_columns if _normalize_key(col) in REQUEST_ID_KEYS]
    body["requestId"] = _get_first_value(row, request_id_columns) or body.get("object_id") or body.get("objectId") or "NA"
    return body


def process_excel(file):
    try:
        df = pd.read_excel(file)
    except Exception as e:
        LOGGER.error(f"Error reading Excel file: {e}")
        raise ValueError("Uploaded file is not a valid Excel file or is corrupted.") from e

    df = df.dropna(how="all")
    payloads = []

    for i, row in df.iterrows():
        try:
            # Clean the row data: Remove NaN values and convert keys to strings
            clean_row = {str(k): v for k, v in row.items() if pd.notna(v)}

            # Build body using existing helper function
            body = _build_body(row, df.columns)
            if not body:
                continue

            request_id = body["requestId"]

            # Find columns with flexible normalization
            method_columns = [col for col in df.columns if _normalize_key(col) == "method"]
            path_columns = [col for col in df.columns if _normalize_key(col) == "path"]
            value_columns = [col for col in df.columns if _normalize_key(col) == "value"]

            # Extract values with defaults
            method = _get_first_value(row, method_columns) or "POST"
            path = _get_first_value(row, path_columns) or "/auth/v1/add_update_user/"
            auth_token = _get_first_value(row, value_columns) or "Bearer test"

            # Build the operation payload
            payload = {
                "body": body,
                "requestId": request_id,
                "method": method,
                "path": path,
                "headers": [
                    {
                        "name": "Authorization",
                        "value": auth_token,
                    }
                ],
            }
            payloads.append(payload)

        except Exception as e:
            LOGGER.error(f"Error processing row {i}: {e}")

    batch_request = {
        **DEFAULT_BATCH_REQUEST,
        "operations": payloads,
    }
    return json.dumps(batch_request, indent=4)


def download_sample(request):
    file_path = os.path.join(
        settings.BASE_DIR,
        "https://docs.google.com/spreadsheets/d/1jcDsu68BT4WpqIaVUr-Y3XsLZ7eXdYCwKDh2frsqFOI/edit?usp=sharingx",
    )
    if os.path.exists(file_path):
        return FileResponse(open(file_path, "rb"), as_attachment=True, filename="sample.xlsx")
    raise Http404("File not found")


def upload_file(request):
    json_data = None
    error_message = None

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES["file"]
            try:
                json_data = process_excel(uploaded_file)
            except ValueError as exc:
                error_message = str(exc)
            except Exception:
                error_message = "An unexpected error occurred while processing your file."
    else:
        form = UploadFileForm()

    return render(
        request,
        "converter/upload.html",
        {
            "form": form,
            "json_data": json_data,
            "error_message": error_message,
        },
    )
