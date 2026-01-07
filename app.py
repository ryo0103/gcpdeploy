import streamlit as st
from google.cloud import storage as gcs

st.title("GCS テスト")
project_id = "gcp-deploy-mock0106"
uploaded = st.file_uploader("ファイルを選択")
if uploaded is not None:
    client = gcs.Client(project_id)
    [print(bucket.name) for bucket in client.list_buckets()]