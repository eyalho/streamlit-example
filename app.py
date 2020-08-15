import streamlit as st
import pandas as pd

from download_file_hack import download_link
from process_file import process

UPLOADED_FILE_NAME = "upload.csv"
DOWNLOAD_FILE_NAME = "download.csv"

st.title("Yahel's POC")
st.write("Here's our first attempt: Uploading a file and process it")

st.set_option('deprecation.showfileUploaderEncoding',
              False)  # this line delete the alert of API future change (it won't be needed anymore soon)

uploaded_file = st.file_uploader("Upload a csv file...", type="csv")

if uploaded_file is not None:
    # use panda to read csv into DataFrame object

    data = pd.read_csv(uploaded_file)
    uploaded_file.close()

    # show content of uploaded file
    # Read this in order to choose specific font style.. https://www.w3schools.com/html/html_styles.asp
    st.markdown('<p style="color:blue;">Uploaded csv 10 first rows are:</p>', unsafe_allow_html=True)
    st.dataframe(data.head(10))

    # save into a local file on the server. consider adding a timestamp or some uniq ID to filename.
    data.to_csv(UPLOADED_FILE_NAME)

    # process the local file
    processed_data = process(UPLOADED_FILE_NAME)

    # show content of file to download
    st.markdown(f'<p style="font-size:50px;color:green;">Finished processing</p>', unsafe_allow_html=True)

    st.markdown(f'<p style="color:blue;">{process.__doc__}<br>10 first rows are:</p>', unsafe_allow_html=True)
    st.dataframe(processed_data.head(10))

    tmp_download_link = download_link(processed_data, DOWNLOAD_FILE_NAME, 'Click here to download the result csv!')
    st.markdown(tmp_download_link, unsafe_allow_html=True)
