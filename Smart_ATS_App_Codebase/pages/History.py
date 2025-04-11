import streamlit as st
from utils.firebase import db, is_logged_in
import pandas as pd

st.set_page_config(page_title="History | Smart ATS")

st.title("📜 Resume Evaluation History")

if not is_logged_in():
    st.warning("⚠️ You must be logged in to view your history.")
    st.stop()

# User's email ID
user_email = st.session_state['user']

# Fetch all resumes from Firebase DB
data = db.child("resumes").get()

if not data.each():
    st.info("No evaluations found yet. Submit a resume first.")
else:
    # Filter entries by user
    user_history = []
    for item in data.each():
        record = item.val()
        if record.get("user_id") == user_email:
            user_history.append(record)

    if len(user_history) == 0:
        st.info("No evaluations found for this account.")
    else:
        df = pd.DataFrame(user_history)
        df = df.sort_values(by="timestamp", ascending=False)
        st.dataframe(df[["timestamp", "job_title", "resume_score", "missing_keywords", "profile_summary"]])
