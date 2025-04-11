import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.gemini_api import get_gemini_response

input_prompt_template = """
Hey Act Like a skilled or very experienced ATS(Application Tracking System)
with a deep understanding of tech field, software engineering, data science, data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving the resumes. Assign the percentage Matching based 
on JD and the missing keywords with high accuracy

resume: {text}
description: {jd}

I want the response in the structure:
JD Match:  %  
Missing Keywords: []  
Profile Summary: ""

Note: Please do not include any other information in the response.
"""

def run():
    st.title("📄 Resume Evaluator")
    jd = st.text_area("Paste the Job Description")
    uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type="pdf")

    if st.button("Evaluate"): 
        if uploaded_file is not None:
            text = extract_text_from_pdf(uploaded_file)
            prompt = input_prompt_template.format(text=text, jd=jd)
            response = get_gemini_response(prompt)
            st.subheader("🔍 ATS Evaluation Result")
            st.write(response)
        else:
            st.warning("⚠️ Please upload a PDF resume.")
