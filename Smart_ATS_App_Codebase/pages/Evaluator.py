import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.gemini_api import get_gemini_response

jd_prompt_template = """
Hey Act Like a skilled or very experienced ATS (Application Tracking System)
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

general_prompt_template = """
You're an experienced resume analyst and career advisor. Analyze the resume below and provide a constructive evaluation. Focus on structure, clarity, tone, action verbs, quantifiable achievements, and formatting best practices. 

Give your response in this format:
- Overall Score: /100
- Strengths: 
- Areas for Improvement: 
- Suggestions for Better Impact:

Resume:
{text}
"""

def run():
    st.title("📄 Resume Evaluator")

    eval_mode = st.radio("Choose Evaluation Type", ["With Job Description", "Without Job Description (General Resume Check)"])
    
    uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type="pdf")

    if eval_mode == "With Job Description":
        jd = st.text_area("Paste the Job Description", height=200)
    
    if st.button("🔍 Evaluate Resume"):
        if uploaded_file is not None:
            resume_text = extract_text_from_pdf(uploaded_file)
            
            if eval_mode == "With Job Description":
                if not jd.strip():
                    st.warning("⚠️ Please paste the Job Description to continue.")
                    return
                prompt = jd_prompt_template.format(text=resume_text, jd=jd)
            else:
                prompt = general_prompt_template.format(text=resume_text)

            with st.spinner("Evaluating your resume..."):
                result = get_gemini_response(prompt)

            st.subheader("✅ Evaluation Result")
            st.markdown(result)

        else:
            st.warning("⚠️ Please upload a resume to continue.")
