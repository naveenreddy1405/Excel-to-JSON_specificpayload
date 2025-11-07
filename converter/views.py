import pandas as pd
import json
from datetime import datetime
from django.shortcuts import render
from .forms import UploadFileForm
from django.http import FileResponse, Http404
import os
from django.conf import settings


import logging
from datetime import datetime
import pandas as pd
import json

import logging
from datetime import datetime
import pandas as pd
import json

def process_excel(file):
    try:
        df = pd.read_excel(file)
    except Exception as e:
        logging.error(f"Error reading Excel file: {e}")
        raise ValueError("Uploaded file is not a valid Excel file or is corrupted.")

    df = df.dropna(how='all')

    fixed_keys = {'object_id', 'object_type', 'userId', 'objectId', 'requestId', 'method', 'path', 'value'}
    excluded_keys = {'name', 'requestId.1'}


    
    
    
    payloads = []

    for i, row in df.iterrows():
        try:
            body = {}

            # Validate mandatory IDs
            if 'object_id' in df.columns and pd.notna(row.get('object_id')):
                body['object_id'] = str(row.get('object_id')).strip()
                body['object_type'] = 'Reports'
            elif 'objectId' in df.columns and pd.notna(row.get('objectId')):
                body['objectId'] = str(row.get('objectId')).strip()
                body['objectType'] = str(row.get('objectType', 'Transaction')).strip()
            elif 'userId' in df.columns and pd.notna(row.get('userId')):
                body['userId'] = str(row.get('userId')).strip()
            else:
                continue  # Skip row if no recognized ID

            # Add dynamic fields except fixed and excluded keys and metaFields
            for col in df.columns:
                if col not in fixed_keys and col not in excluded_keys and not col.startswith('metaFields.') and pd.notna(row.get(col)):
                    body[col] = str(row.get(col)).strip()

            # Handle metaFields
            meta_columns = [col for col in df.columns if col.startswith('metaFields.')]
            metaDict = {}
            for col in meta_columns:
                val = row[col]
                if pd.notna(val):
                    key = col.replace('metaFields.', '')
                    if isinstance(val, (pd.Timestamp, datetime)):
                        val = val.strftime('%Y-%m-%d')
                    else:
                        val = str(val)
                    metaDict[key] = val
            if metaDict:
                body['metaFields'] = metaDict

            # Set requestId inside body
            request_id_from_excel = row.get('requestId') or row.get('requestId.1')
            if request_id_from_excel and pd.notna(request_id_from_excel):
                body['requestId'] = str(request_id_from_excel).strip()
            else:
                body['requestId'] = body.get('object_id') or body.get('objectId') or 'NA'

            requestId = body['requestId']
            method = str(row.get('method', 'POST')).strip()
            path = str(row.get('path', '/auth/v1/add_update_user/')).strip()
            auth_token = str(row.get('value', 'Bearer test')).strip()

            payload = {
                'body': body,
                'requestId': requestId,
                'method': method,
                'path': path,
                'headers': [
                    {
                        'name': 'Authorization',
                        'value': auth_token
                    }
                ]
            }
            payloads.append(payload)

        except Exception as e:
            logging.error(f"Error processing row {i}: {e}")
            # You may choose to continue or raise here
        batch_request = {
            "batch_request_id": "update test1",
            "batch_update_url": "https://client-api-domain.com/batch_status_update/",
            "operations": payloads
        }

    return json.dumps(batch_request, indent=4)





def download_sample(request):
    file_path = os.path.join(settings.BASE_DIR, "https://docs.google.com/spreadsheets/d/1jcDsu68BT4WpqIaVUr-Y3XsLZ7eXdYCwKDh2frsqFOI/edit?usp=sharingx")  # Adjust path if needed
    if os.path.exists(file_path):
        return FileResponse(open(file_path, "rb"), as_attachment=True, filename="sample.xlsx")
    else:
        raise Http404("File not found")


def upload_file(request):
    json_data = None
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            json_data = process_excel(uploaded_file)
    else:
        form = UploadFileForm()
    return render(request, 'converter/upload.html', {'form': form, 'json_data': json_data})
