import os
from typing import Optional
from google.cloud import storage

_client: Optional[storage.Client] = None
_bucket = None

def _init():
  global _client, _bucket
  if _client is None:
    _client = storage.Client()
  if _bucket is None:
    bucket_name = os.environ.get("GCS_BUCKET_NAME")
    if not bucket_name:
      raise RuntimeError("環境変数 GCS_BUCKET_NAME が設定されていません")
    _bucket = _client.bucket(bucket_name)

def upload_bytes(dest_path: str, data: bytes, content_type: Optional[str] = None) -> None:
  _init()
  blob = _bucket.blob(dest_path)
  blob.upload_from_string(data, content_type=content_type)

def download_bytes(path: str) -> bytes:
  _init()
  blob = _bucket.blob(path)
  if not blob.exists():
    raise FileNotFoundError(f"GCS object not found: {path}")
  return blob.download_as_bytes()