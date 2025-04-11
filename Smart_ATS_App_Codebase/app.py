import streamlit as st
from pages import Evaluator, Enhancer, Templates, Insights

def main():
    st.set_page_config(page_title="Smart ATS", layout="wide")
    st.sidebar.title("Smart ATS Navigation")
    page = st.sidebar.radio("Go to", ["Resume Evaluator", "Resume Enhancer", "Resume Templates", "Insights Dashboard"])

    if page == "Resume Evaluator":
        Evaluator.run()
    elif page == "Resume Enhancer":
        Enhancer.run()
    elif page == "Resume Templates":
        Templates.run()
    elif page == "Insights Dashboard":
        Insights.run()

if __name__ == "__main__":
    main()
