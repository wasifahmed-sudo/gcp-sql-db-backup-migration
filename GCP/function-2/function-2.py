import boto3
import os
from google.cloud import storage

def gcs_to_s3(event, context):
    # Google Cloud Storage configuration
    gcs_bucket_name = event['bucket']
    file_name = event['name']

    # AWS S3 configuration
    aws_access_key = os.environ.get('AWS_ACCESS_KEY_ID')
    aws_secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
    s3_bucket_name = os.environ.get('S3_Bucket')
    s3_client = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

    try:
        # Download file from GCS to /tmp directory
        storage_client = storage.Client()
        gcs_bucket = storage_client.bucket(gcs_bucket_name)
        blob = gcs_bucket.blob(file_name)
        blob.download_to_filename(f'/tmp/{file_name}')

        # Upload file from /tmp directory to S3 bucket
        s3_client.upload_file(f'/tmp/{file_name}', s3_bucket_name, file_name)

        # Delete file from GCS bucket after successful upload to S3 bucket
        blob.delete()

        return f"File transferred from GCS to S3: {file_name} -> {s3_bucket_name}/{file_name}"
    
    except Exception as e:
        return f"Error: {str(e)}"