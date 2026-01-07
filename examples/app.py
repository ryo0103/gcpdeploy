import streamlit as st
from GCSWrapper import GCSWrapper

gcs = GCSWrapper()
uploaded = st.file_uploader("アップロードするファイルを選択")

if uploaded is not None:
    if st.button("GCSにアップロード"):
        gcs.upload(uploaded,uploaded.name)

names = gcs.get_file_names()
if not names:
    st.write("ファイルがありません")
else:
    selected_file = st.selectbox("ダウンロードするファイルを選択",names)
    if selected_file:
        data = gcs.download(selected_file)
        st.download_button(label="ローカルに保存",data=data,file_name=selected_file)