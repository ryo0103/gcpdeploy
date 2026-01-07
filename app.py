import streamlit as st
from google.cloud import storage as gcs

st.title("GCS Mock")
uploaded = st.file_uploader("ファイルを選択")
client = gcs.Client()
print(len(client.list_buckets()))
print(client.list_buckets())