import streamlit as st
from google.cloud import storage as gcs
import os

st.title("GCS Mock")
uploaded = st.file_uploader("ファイルを選択")
client = gcs.Client()
st.write(os.environ["GCS_BUCKET_NAME"])
# st.write([bucket.name for bucket in list(client.list_buckets())])