from google.cloud import storage as gcs
import os

class GCSWrapper:
    def __init__(self):
        bucket_name = os.environ["GCS_BUCKET_NAME"]
        self._client = gcs.Client()
        self._bucket = self._client.bucket(bucket_name)

    def get_file_names(self):
        return [file.name for file in self._client.list_blobs(self._bucket)]
    
    def upload(self,file,file_name):
        gcs_path = f"{file_name}"
        blob = self._bucket.blob(gcs_path)
        blob.upload_from_file(file, rewind=True)
    
    def download(self,file_name):
        gcs_path = f"{file_name}"
        blob = self._bucket.blob(gcs_path)
        return blob.download_as_bytes()