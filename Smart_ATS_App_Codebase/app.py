import streamlit as st
st.set_page_config(page_title="Smart ATS", layout="wide")  # ✅ FIRST!

from pages import Evaluator, Enhancer, Templates, Insights, Login, History

def main():
    st.sidebar.title("Smart ATS Navigation")
    page = st.sidebar.radio("Go to", ["Login", "Resume Templates", "Resume Enhancer", "Resume Evaluator", "Insights Dashboard", "History"])

    if page == "Resume Evaluator":
        Evaluator.run()
    elif page == "Resume Enhancer":
        Enhancer.run()
    elif page == "Resume Templates":
        Templates.run()
    elif page == "Insights Dashboard":
        Insights.run()
    elif page == "Login":
        Login.login_btn
        Login.signup_btn
    elif page == "History":
        History.run()
    else:
        st.write("Select a page from the sidebar to get started.")

if __name__ == "__main__":
    main()
