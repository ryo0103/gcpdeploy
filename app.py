import streamlit as st
from gcs_client import upload_bytes, download_bytes

st.title("GCS ファイルアップロード")

uploaded = st.file_uploader("ファイルを選択")
if uploaded is not None:
    dest_path = f"uploads/{uploaded.name}"
    upload_bytes(dest_path, uploaded.read(), content_type=uploaded.type)
    st.success(f"アップロード完了: {dest_path}")