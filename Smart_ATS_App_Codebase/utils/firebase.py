import pyrebase
import os
from dotenv import load_dotenv
import streamlit as st
from datetime import datetime

# Load environment variables
load_dotenv()

firebaseConfig = {
    "apiKey": os.getenv("API_KEY"),
    "authDomain": os.getenv("AUTH_DOMAIN"),
    "databaseURL": os.getenv("DATABASE_URL"),
    "projectId": os.getenv("PROJECT_ID"),
    "storageBucket": os.getenv("STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("MESSAGING_SENDER_ID"),
    "appId": os.getenv("APP_ID")
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

# Session helpers
def save_user_session(email):
    st.session_state['user'] = email

def is_logged_in():
    return 'user' in st.session_state

# Save history to database
def save_resume_history(user_id, job_title, score, keywords, summary):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db.child("resumes").push({
        "user_id": user_id,
        "job_title": job_title,
        "resume_score": score,
        "missing_keywords": keywords,
        "profile_summary": summary,
        "timestamp": timestamp
    })
