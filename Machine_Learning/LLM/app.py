import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json
import time

load_dotenv()  # Load all environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-2.0-flash-thinking-exp')
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += str(page.extract_text())
    return text

def format_prompt(resume_text, jd_text):
    return f"""
Hey Act Like a skilled or very experienced ATS (Application Tracking System)
with a deep understanding of tech field, software engineering, data science, data analyst,
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
the best assistance for improving the resumes. Assign the percentage Matching based 
on JD and the missing keywords with high accuracy.

resume: {resume_text}
description: {jd_text}

I want the response in the structure:
JD Match:  %  
Missing Keywords: []  
Profile Summary: ""

Note: Please do not include any other information in the response.
"""

# Streamlit app
st.title("📄 Smart ATS")
st.text("🚀 Improve Your Resume for ATS Screening")

jd = st.text_area("📌 Paste the Job Description")
uploaded_file = st.file_uploader("📁 Upload Your Resume (PDF only)", type="pdf", help="Please upload a PDF file")

if st.button("Submit"):
    if uploaded_file is not None and jd.strip() != "":
        resume_text = input_pdf_text(uploaded_file)
        full_prompt = format_prompt(resume_text, jd)
        
        with st.spinner("Analyzing your resume with Gemini AI..."):
            response_text = get_gemini_response(full_prompt)

        st.subheader("🎯 ATS Evaluation Result")
        
        # Streaming effect
        placeholder = st.empty()
        final_output = ""
        for char in response_text:
            final_output += char
            placeholder.markdown(f"```\n{final_output}\n```")  # code block style
            time.sleep(0.01)  # control typing speed
    else:
        st.warning("⚠️ Please upload a resume and provide a job description.")
