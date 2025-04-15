import streamlit as st
from utils.firebase import auth, save_user_session

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state["page"] = "login"  # Default page is login

# Define the login/signup page
def login_page():
    st.title("🔐 Login to Smart ATS")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    col1, col2 = st.columns([1, 1])
    login_btn = col1.button("Login")
    signup_btn = col2.button("Sign Up")

    if login_btn:
        if not email or not password:
            st.error("Email and password cannot be empty.")
        else:
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                save_user_session(email)
                st.success("Logged in successfully ✅")
                # Navigate to Evaluator page
                st.session_state["page"] = "evaluator"
            except Exception as e:
                st.error(f"Login failed: {str(e)}")

    if signup_btn:
        if not email or not password:
            st.error("Email and password cannot be empty.")
        elif len(password) < 6:
            st.error("Password must be at least 6 characters long.")
        else:
            try:
                user = auth.create_user_with_email_and_password(email, password)
                save_user_session(email)
                st.success("Account created! Logged in 🎉")
                # Navigate to Evaluator page
                st.session_state["page"] = "evaluator"
            except Exception as e:
                st.error(f"Signup failed: {str(e)}")

# Define the Evaluator page
def evaluator_page():
    st.title("📊 Evaluator Page")
    st.write("Welcome to the Evaluator page!")
    # Add logout button
    if st.button("Logout"):
        del st.session_state["page"]  # Clear session state for navigation
        st.experimental_rerun()  # Reload the app

# Render pages based on session state
if st.session_state["page"] == "login":
    login_page()
elif st.session_state["page"] == "evaluator":
    evaluator_page()
