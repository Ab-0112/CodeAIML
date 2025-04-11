import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.gemini_api import get_gemini_response
from utils.text_streamer import stream_text

def generate_enhancer_prompt(resume_text):
    return f"""
Act like a professional resume coach and AI assistant. Your job is to improve the given resume by rewriting bullet points with stronger action verbs, quantifiable impact, and clearer formatting.

Provide suggestions in this format:

Section: Work Experience  
Original: "Worked on data visualization tools"  
Improved: "Developed dynamic data dashboards using Tableau, improving reporting efficiency by 40%"

Make suggestions for each weak point you find. Do NOT rewrite the entire resume — just give smart bullet-level enhancements.

Resume:
{resume_text}
"""

def run():
    st.title("🛠️ Resume Enhancer")
    uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type="pdf")

    if st.button("✨ Enhance"):
        if uploaded_file is not None:
            resume_text = extract_text_from_pdf(uploaded_file)
            prompt = generate_enhancer_prompt(resume_text)
            with st.spinner("Enhancing your resume..."):
                response = get_gemini_response(prompt)
            st.subheader("🚀 Suggestions to Level Up Your Resume")
            stream_text(response)
        else:
            st.warning("⚠️ Please upload your resume to continue.")

