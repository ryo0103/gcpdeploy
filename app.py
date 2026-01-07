import streamlit as st
import os
from GCSWrapper import GCSWrapper

st.title("GCS Mock")
uploaded = st.file_uploader("ファイルを選択")
gcs = GCSWrapper()
if uploaded is not None:
    gcs.upload(uploaded,uploaded.name)
    for s in gcs.get_file_names():
        st.write(s)