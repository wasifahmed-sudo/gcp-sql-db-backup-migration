import googleapiclient.discovery

def backup_database(event, context):
    project_id = '$project_id'
    instance_id = '$nstance_id'
    bucket_name = '$bucket_name'
    sqladmin = googleapiclient.discovery.build('sqladmin', 'v1beta4')

    uri = f'gs://{bucket_name}/backup-{context.timestamp}.sql'
    body = {
        'exportContext': {
            'kind': 'sql#exportContext',
            'fileType': 'SQL',
            'uri': uri,
            'databases': ['postgres']
        }
    }

    request = sqladmin.instances().export(project=project_id, instance=instance_id, body=body)
    request.execute()
