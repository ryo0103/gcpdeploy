import streamlit as st
from google.cloud import storage as gcs

st.title("GCS テスト")
project_id = "gcp-deploy-mock0106"
uploaded = st.file_uploader("ファイルを選択")
client = gcs.Client()
[print(bucket) for bucket in client.list_buckets()]