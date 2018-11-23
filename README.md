# Google Cloud Render Template Serverless

This sample demonstrates how to render a template form from Google Storage using Cloud Functions.


## Functions Code

Form Template
See file [functions/gcf-form-template/main.py](functions/gcf-form-template/main.py) for the code.
The dependencies are listed in [functions/gcf-form-template/requirements.txt](functions/gcf-upload-file/requirements.txt).

## Trigger rules

The functions triggers on http request.

## Setting up the sample

This sample comes with a Function and web-based UI for testing the function. To configure it:

 1. Create a Google Cloud Project using the [Console GCP](https://console.cloud.google.com)
 1. Create billing account [Console Billing](https://console.cloud.google.com/billing/)
 1. Enable the Cloud Functions API [Console Cloud Functions](https://console.cloud.google.com/functions/)
 1. Enable the Cloud Storage API [Console Cloud Storage](https://console.cloud.google.com/storage/)


## Deploy and test

To test the sample:
 1. Download and install gcloud command line tool [Console](https://cloud.google.com/sdk/install)
 2. From function path [functions/gcf-render-template/](functions/gcf-render-template/) execute:
 ```
 export FUNCTION_NAME="gcf-form-template";
 export PATH_FILE="gcf-form-template.html";
 export BUCKET_NAME="gcf-static-files";
 gcloud beta functions deploy ${FUNCTION_NAME} --entry-point execute --set-env-vars BUCKET_NAME=${BUCKET_NAME},PATH_FILE=${PATH_FILE} --memory 128MB --runtime python37 --trigger-http;
 ```
 3. Return something like that:
```
Deploying function (may take a while - up to 2 minutes)...done.                                                                                                                                            
availableMemoryMb: 128
entryPoint: execute
httpsTrigger:
  url: https://[region]-[project id].cloudfunctions.net/gcf-form-template
labels:
  deployment-tool: cli-gcloud
name: projects/[project id]/locations/[region]/functions/gcf-form-template
runtime: python37
serviceAccountEmail: [service account email]
status: ACTIVE
timeout: 60s
updateTime: '2018-11-22T16:05:07Z'
versionId: '1'
```
