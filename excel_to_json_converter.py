#!/usr/bin/env python3
"""
Excel to JSON Converter - Standalone CLI Tool
Converts Excel files to JSON batch request format

Usage:
    python excel_to_json_converter.py input.xlsx output.json
    python excel_to_json_converter.py input.xlsx  # outputs to input_output.json
"""

import argparse
import json
import logging
import os
import re
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd


# Configuration
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

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
LOGGER = logging.getLogger(__name__)


# Helper Functions
def _strip_duplicate_suffix(column_name):
    """Remove pandas duplicate suffixes like .1, .2, etc."""
    return PANDAS_DUPLICATE_SUFFIX.sub("", str(column_name).strip())


def _normalize_key(column_name):
    """Normalize column names: lowercase, remove spaces/underscores"""
    base_name = _strip_duplicate_suffix(column_name)
    return re.sub(r"[\s_]+", "", base_name).lower()


def _is_meta_field(column_name):
    """Check if column is old format metafield (metaFields.fieldName)"""
    return _normalize_key(column_name).startswith("metafields.")


def _meta_field_name(column_name):
    """Extract field name from metaFields.fieldName format"""
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
    """Check if cell has meaningful content"""
    return pd.notna(value) and str(value).strip() != ""


def _stringify_value(value):
    """Convert value to string, formatting dates as YYYY-MM-DD"""
    if isinstance(value, (pd.Timestamp, datetime)):
        return value.strftime("%Y-%m-%d")
    return str(value).strip()


def _get_first_value(row, columns):
    """Get first non-empty value from list of columns"""
    for column in columns:
        value = row.get(column)
        if _cell_has_value(value):
            return _stringify_value(value)
    return None


def _build_body(row, df_columns):
    """Build JSON body object from row data"""
    body = {}

    # Find ID columns (supports legacy and new naming)
    object_id_columns = [col for col in df_columns if _normalize_key(col) == "objectid"]
    legacy_object_id_columns = [col for col in df_columns if str(_strip_duplicate_suffix(col)).strip() == "object_id"]
    user_id_columns = [col for col in df_columns if _normalize_key(col) == "userid"]
    object_type_columns = [col for col in df_columns if _normalize_key(col) == "objecttype"]

    # Get ID values
    legacy_object_id = _get_first_value(row, legacy_object_id_columns)
    object_id = _get_first_value(row, object_id_columns)
    user_id = _get_first_value(row, user_id_columns)

    # Set appropriate ID fields
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

    # Get metafield columns using position-based detection
    metafield_cols = _get_metafield_columns(df_columns)

    # Add regular columns to body
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
    # Skip columns that are already in old format to avoid duplicates
    for column in metafield_cols:
        if _is_meta_field(column):
            continue
            
        value = row.get(column)
        if not _cell_has_value(value):
            continue
        
        meta_fields[_strip_duplicate_suffix(column)] = _stringify_value(value)

    if meta_fields:
        body["metaFields"] = meta_fields

    # Set request ID
    request_id_columns = [col for col in df_columns if _normalize_key(col) in REQUEST_ID_KEYS]
    body["requestId"] = _get_first_value(row, request_id_columns) or body.get("object_id") or body.get("objectId") or "NA"
    
    return body


def process_excel(file_path):
    """
    Process Excel file and return batch request JSON structure
    
    Args:
        file_path: Path to Excel file
        
    Returns:
        dict: Batch request with all converted rows
    """
    try:
        df = pd.read_excel(file_path)
        LOGGER.info(f"Successfully read Excel file: {file_path}")
        LOGGER.info(f"Found {len(df)} rows and {len(df.columns)} columns")
    except Exception as e:
        LOGGER.error(f"Error reading Excel file: {e}")
        raise ValueError("Uploaded file is not a valid Excel file or is corrupted.") from e

    df = df.dropna(how="all")
    payloads = []

    for i, row in df.iterrows():
        try:
            # Build body using helper function
            body = _build_body(row, df.columns)
            if not body:
                LOGGER.debug(f"Row {i+1}: Skipped (no valid ID found)")
                continue

            payloads.append(body)
            LOGGER.debug(f"Row {i+1}: Converted successfully")

        except Exception as e:
            LOGGER.error(f"Error processing row {i+1}: {e}")
            continue

    # Build batch request
    batch_request = DEFAULT_BATCH_REQUEST.copy()
    batch_request["requests"] = payloads

    LOGGER.info(f"Successfully converted {len(payloads)} rows")
    
    return batch_request


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description='Convert Excel files to JSON batch request format',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python excel_to_json_converter.py input.xlsx output.json
  python excel_to_json_converter.py input.xlsx  # outputs to input_output.json
  python excel_to_json_converter.py input.xlsx -v  # verbose output
        '''
    )
    
    parser.add_argument('input_file', help='Input Excel file path')
    parser.add_argument('output_file', nargs='?', help='Output JSON file path (default: input_output.json)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose logging')
    parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print JSON (default: compact)')
    
    args = parser.parse_args()
    
    # Set logging level
    if args.verbose:
        LOGGER.setLevel(logging.DEBUG)
    
    # Validate input file
    input_path = Path(args.input_file)
    if not input_path.exists():
        LOGGER.error(f"Input file not found: {args.input_file}")
        sys.exit(1)
    
    if input_path.suffix.lower() not in ['.xlsx', '.xls']:
        LOGGER.error(f"Input file must be Excel format (.xlsx or .xls): {args.input_file}")
        sys.exit(1)
    
    # Determine output path
    if args.output_file:
        output_path = Path(args.output_file)
    else:
        output_path = input_path.parent / f"{input_path.stem}_output.json"
    
    try:
        LOGGER.info(f"Starting conversion...")
        LOGGER.info(f"Input: {input_path}")
        LOGGER.info(f"Output: {output_path}")
        
        # Process the Excel file
        batch_request = process_excel(str(input_path))
        
        # Write JSON output
        with open(output_path, 'w', encoding='utf-8') as f:
            indent = 2 if args.pretty else None
            json.dump(batch_request, f, indent=indent, ensure_ascii=False)
        
        LOGGER.info(f"✅ Conversion complete!")
        LOGGER.info(f"Output saved to: {output_path}")
        LOGGER.info(f"Total requests: {len(batch_request.get('requests', []))}")
        
    except Exception as e:
        LOGGER.error(f"❌ Conversion failed: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
