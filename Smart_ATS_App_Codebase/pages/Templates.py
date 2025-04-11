import streamlit as st
import pdfkit

# Optional: Configure wkhtmltopdf if running locally
# pdfkit_config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')

def html_resume_template(name, email, phone, linkedin, github, summary, experience, education, skills):
    return f"""
    <html><body>
    <h2>{name}</h2>
    <p>{email} | {phone}</p>
    <p>{linkedin} | {github}</p>
    <h3>Profile Summary</h3><p>{summary}</p>
    <h3>Work Experience</h3><p>{experience}</p>
    <h3>Education</h3><p>{education}</p>
    <h3>Skills</h3><p>{skills}</p>
    </body></html>
    """

def run():
    st.title("🧾 Resume Templates")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    linkedin = st.text_input("LinkedIn URL")
    github = st.text_input("GitHub URL")
    summary = st.text_area("Profile Summary")
    experience = st.text_area("Work Experience", height=150)
    education = st.text_area("Education")
    skills = st.text_area("Skills (comma-separated)")

    if st.button("📄 Generate Resume Preview"):
        st.markdown("---")
        st.subheader("📄 Preview: Classic Resume Template")

        st.markdown(f"### {name}")
        st.markdown(f"📧 {email} | 📞 {phone}")
        st.markdown(f"[LinkedIn]({linkedin}) | [GitHub]({github})")

        st.markdown("#### Profile Summary")
        st.markdown(summary)
        st.markdown("#### Work Experience")
        st.markdown(experience)
        st.markdown("#### Education")
        st.markdown(education)
        st.markdown("#### Skills")
        st.markdown(f"`{skills}`")

        resume_html = html_resume_template(name, email, phone, linkedin, github, summary, experience, education, skills)

        with open("resume.html", "w", encoding="utf-8") as f:
            f.write(resume_html)

        import pdfkit

        path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # Make sure this path is correct
        config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

        pdfkit.from_file("resume.html", "resume.pdf", configuration=config)


        with open("resume.pdf", "rb") as f:
            st.download_button("⬇️ Download Resume as PDF", f, file_name="Your_Resume.pdf")
