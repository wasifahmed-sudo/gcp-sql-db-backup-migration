# Workflow Explanation

When the scheduled cron job initiates, function-1 is activated. This function orchestrates the process of creating a backup of the database and subsequently storing the backup file in a Google Cloud Storage (GCS) bucket. 

This event triggers function-2, configured to respond to changes in the GCS bucket. function-2 is responsible for migrating the backup file to an AWS S3 bucket. Upon successful migration, the file is then deleted from the GCS bucket. This synchronized workflow ensures a seamless and automated process for backing up the database and efficiently managing the storage locations.
