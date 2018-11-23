from google.cloud import storage
from google.cloud.storage import Blob
from flask import Flask, Response, render_template_string

import google
import os

# Global Vars
PROJECT_ID = os.environ.get('GCP_PROJECT', None)
REGION = os.environ.get('FUNCTION_REGION', None)

# Dinamic Vars
PATH_FILE = os.environ.get('PATH_FILE', None)
BUCKET_NAME = os.environ.get('BUCKET_NAME', None)
PARAMS = os.environ.get('PARAMS', {})

# Check env vars
if not PATH_FILE or not BUCKET_NAME:
    print('Export env vars: PATH_FILE and BUCKET_NAME')
    raise # Circuit break
    
def execute(request):
    # Get bucket
    try: 
        client_storage = storage.Client()
        bucket = client_storage.get_bucket(BUCKET_NAME)
    except Exception as e: # Any exception
        return (u'Error: %s' % e, 500)

    # Get File
    blob = Blob(name=PATH_FILE, bucket=bucket)
    response = blob.download_as_string().decode()

    # Response
    return render_template_string(response, **PARAMS)