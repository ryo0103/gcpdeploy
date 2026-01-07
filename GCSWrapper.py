from google.cloud import storage as gcs
import os

class GCSWrapper:
    def __init__(self):
        self._client = gcs.Client()
        self._bucket = self._client.get_bucket(os.environ["GCS_BUCKET_NAME"])

    def get_file_names(self):
        return [file for file in self._client.list_blobs(self._bucket)]
    
    def upload(self,file,file_name):
        gcs_path = f"uploads/{file_name}"
        blob = self._bucket.blob(gcs_path)
        blob.upload_from_file(file, rewind=True)
        