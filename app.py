import streamlit as st
import requests

st.title("AI Resume Job Matcher")

uploaded_file = st.file_uploader(
    "Upload Resume Image",
    type=["png","jpg","jpeg"]
)

if uploaded_file is not None:

    st.image(uploaded_file, caption="Uploaded Resume")

    if st.button("Analyze Resume"):

        url = "http://127.0.0.1:8000/predict"

        files = {
            "file": uploaded_file.getvalue()
        }

        response = requests.post(url, files={"file": uploaded_file})

        result = response.json()

        st.success("Predicted Job Role")

        st.write(result["predicted_job_category"])

        st.subheader("Extracted Resume Text")

        st.write(result["extracted_text_sample"])