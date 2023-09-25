import sys
from google.cloud import storage

def get_retention_policy(bucket_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    bucket.reload()

    print(f"Bucket Name: {bucket_name}")
    print(f"Retention Policy: {bucket.retention_period} seconds")

if __name__ == "__main__":
    get_retention_policy(bucket_name=sys.argv[1])

