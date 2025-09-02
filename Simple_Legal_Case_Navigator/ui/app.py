import streamlit as st
import requests
from pathlib import Path
from pypdf import PdfReader

API_URL = "http://localhost:8000/ask"

st.title("⚖️ Legal Case Navigator")

# ---- File Uploader ----
st.sidebar.header("📂 Upload Legal Documents")
uploaded_files = st.sidebar.file_uploader(
    "Upload TXT or PDF files", 
    type=["txt", "pdf"], 
    accept_multiple_files=True
)

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

if uploaded_files:
    for file in uploaded_files:
        if file.type == "text/plain":
            text = file.read().decode("utf-8")
        elif file.type == "application/pdf":
            text = extract_text_from_pdf(file)
        else:
            continue
        
        # send ingestion request to backend (you can extend your backend later)
        with open(f"data/{file.name}", "w", encoding="utf-8") as f:
            f.write(text)
        st.sidebar.success(f"✅ {file.name} uploaded and saved!")

# ---- Query Input ----
query = st.text_input("🔍 Enter your legal question")

if st.button("Ask"):
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        response = requests.post(API_URL, json={"query": query, "k": 3})
        if response.status_code == 200:
            data = response.json()
            st.subheader("📖 Answer")
            st.write(data["answer"])
            st.subheader("📂 Relevant Documents")
            for ev in data["evidences"]:
                with st.expander(f"{ev['id']} (score: {ev['score']:.2f})"):
                    st.write(ev["text"])
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
