import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.gemini_api import get_gemini_response
from fpdf import FPDF
import tempfile
import os
import unicodedata  # Added for Unicode sanitization

# Prompt strictly tells Gemini to return resume ONLY, no explanation
def generate_enhancer_prompt(resume_text):
    return f"""
Act like a professional resume writer. Rewrite the following resume to improve formatting, strengthen language, and use action verbs. Keep the structure with professional resume sections (Summary, Experience, Education, Skills, etc.).

⚠️ IMPORTANT: Only return the final rewritten resume in clean plain text format. Do not include ANY explanations, commentary, or extra instructions.

Resume:
{resume_text}
"""

# Function to sanitize any Unicode characters not supported by FPDF (latin-1)
def sanitize_text(text):
    # Normalize to NFKD form, strip out non-latin1 characters
    return unicodedata.normalize("NFKD", text).encode("latin-1", "ignore").decode("latin-1")

def create_pdf(content):
    content = sanitize_text(content)  # ✅ Sanitize before adding to PDF

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    for line in content.split('\n'):
        pdf.multi_cell(0, 10, line)

    temp_dir = tempfile.gettempdir()
    pdf_path = os.path.join(temp_dir, "enhanced_resume.pdf")
    pdf.output(pdf_path)

    return pdf_path

def run():
    st.title("🛠️ Resume Enhancer")
    uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type="pdf")

    if uploaded_file:
        resume_text = extract_text_from_pdf(uploaded_file)
        if st.button("✨ Enhance Resume"):
            prompt = generate_enhancer_prompt(resume_text)

            with st.spinner("Rewriting your resume..."):
                enhanced_resume = get_gemini_response(prompt)

                # Remove Gemini's potential extra notes
                if "**[Your Rewritten Resume Ends Here]**" in enhanced_resume:
                    enhanced_resume = enhanced_resume.split("**[Your Rewritten Resume Ends Here]**")[0]

                if "**[Your Rewritten Resume Starts Here]**" in enhanced_resume:
                    enhanced_resume = enhanced_resume.split("**[Your Rewritten Resume Starts Here]**")[-1]

            st.subheader("✅ Enhanced Resume")
            st.text_area("Preview", enhanced_resume.strip(), height=400)

            # Generate PDF
            pdf_path = create_pdf(enhanced_resume.strip())

            if os.path.exists(pdf_path):
                with open(pdf_path, "rb") as f:
                    file_bytes = f.read()

                st.download_button(
                    label="📄 Download Enhanced Resume (PDF)",
                    data=file_bytes,
                    file_name="enhanced_resume.pdf",
                    mime="application/pdf"
                )
            else:
                st.error("⚠️ PDF generation failed. Please try again.")
    else:
        st.info("👆 Upload your resume to get started!")
