import pandas as pd
import json
from datetime import datetime
from django.shortcuts import render
from .forms import UploadFileForm

def process_excel(file):
    df = pd.read_excel(file, sheet_name="Sheet1")
    df = df.dropna(how='all')
    meta_columns = [col for col in df.columns if col.startswith("metaFields.")]
    payloads = []

    for _, row in df.iterrows():
        metaDict = {}
        for col in meta_columns:
            key = col.replace("metaFields.", "")
            value = row[col]
            if pd.notna(value):
                if isinstance(value, (pd.Timestamp, datetime)):
                    value = value.strftime('%Y-%m-%d')
                else:
                    value = str(value)
            else:
                value = "NA"
            metaDict[key] = value

        auth_token = str(row.get('value', 'Bearer test')).strip()

        if 'userId' in df.columns and pd.notna(row.get('userId')):
            userId = str(row.get('userId')).strip()
            requestId = str(row.get('requestId', userId)).strip()
            method = str(row.get('method', 'POST')).strip()
            path = str(row.get('path', '/auth/v1/add_update_user/')).strip()
            body = {
                "userId": userId,
                "requestId": requestId,
                "metaFields": metaDict
            }

        elif 'objectId' in df.columns and pd.notna(row.get('objectId')):
            objectId = str(row.get('objectId')).strip()
            requestId = str(row.get('requestId', objectId)).strip()
            method = str(row.get('method', 'POST')).strip()
            path = str(row.get('path', '/auth/v1/updateobjectstatus/')).strip()
            objectType = str(row.get('objectType', 'Transaction')).strip()
            body = {
                "objectId": objectId,
                "objectType": objectType,
                "requestId": requestId,
                "metaFields": metaDict
            }
        else:
            continue

        payload = {
            "body": body,
            "requestId": requestId,
            "method": method,
            "path": path,
            "headers": [
                {
                    "name": "Authorization",
                    "value": auth_token
                }
            ]
        }
        payloads.append(payload)

    return json.dumps(payloads, indent=4)


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
