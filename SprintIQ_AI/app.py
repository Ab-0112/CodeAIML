import streamlit as st
import pandas as pd

from crew_setup import run_crew

st.set_page_config(
    page_title="SprintIQ AI",
    layout="wide"
)

st.title("SprintIQ AI")
st.subheader("AI-Powered Agile Sprint Intelligence System")

uploaded_file = st.file_uploader(
    "Upload Agile Sprint Workbook",
    type=["xlsx"]
)

if uploaded_file:

    excel_data = pd.read_excel(
        uploaded_file,
        sheet_name=None
    )

    sheet_names = list(excel_data.keys())

    selected_sheet = st.selectbox(
        "Select Sheet",
        sheet_names
    )

    df = excel_data[selected_sheet]

    st.subheader("Sprint Data Preview")
    st.dataframe(df)

    if st.button("Analyze Sprint"):

        with st.spinner("AI Agents Analyzing Sprint..."):

            data_text = df.to_string()

            result = run_crew(data_text)

        st.subheader("AI Sprint Analysis")

        st.write(result)