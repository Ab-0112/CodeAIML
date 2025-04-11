import streamlit as st
from utils.firebase import auth, save_user_session

st.title("🔐 Login to Smart ATS")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

col1, col2 = st.columns([1, 1])
login_btn = col1.button("Login")
signup_btn = col2.button("Sign Up")

if login_btn:
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        save_user_session(email)
        st.success("Logged in successfully ✅")
        st.switch_page("pages/1_Evaluator.py")
    except Exception as e:
        st.error("Login failed. Please check your credentials.")

if signup_btn:
    try:
        user = auth.create_user_with_email_and_password(email, password)
        save_user_session(email)
        st.success("Account created! Logged in 🎉")
        st.switch_page("pages/1_Evaluator.py")
    except Exception as e:
        st.error("Signup failed. Email may already exist or password too weak.")
