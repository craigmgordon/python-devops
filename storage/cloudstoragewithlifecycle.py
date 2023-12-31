#!/usr/bin/python
# -*- coding: utf-8 -*-
# cloudstoragewithlifecycle.py
# It is an example that handles Cloud Storage buckets on Google Cloud Platform (GCP).
# Create a new Cloud Storage bucket.
# with lifecycle and retention policy 
# You must provide 1 parameter:
# BUCKET_NAME = Name of the bucket

import sys
from google.cloud import storage

def create_bucket_with_policy():
    """_summary_
    """
    project_id = 'devops-project-399815'
    # retention period in seconds
    retention_period = 604800
    storage_location = 'europe-west2'   # Cloud Storage location

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if len(args) < 1:
        print('Not enough parameters.\n'\
              'Proper Usage is: python cloudstoragewithlifecycle.py <BUCKET_NAME>')
        sys.exit(1)

    bucket_name = project_id + '_' + args[0]
    print('Bucket name: ' + bucket_name)

    print('Creating bucket ...')

    # Instantiate the client.
    client = storage.Client()

    try:
        # Instantiate the bucket.
        bucket = client.bucket(bucket_name)
        # Set up lifecycle rules
        bucket.lifecycle_rules = [
            {
                "action": {"type": "SetStorageClass", "storageClass": "NEARLINE"},
                "condition": {"age": 30}
            }
        ]
        # set 7 day retention period
        bucket.retention_period = retention_period
        # Create the bucket object.
        bucket.create(location=storage_location)

        print(f'Bucket {bucket_name} created with retention policy and lifecycle rules.')
    except Exception as err:
        print('Error: ',err)

    return


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    create_bucket_with_policy()





