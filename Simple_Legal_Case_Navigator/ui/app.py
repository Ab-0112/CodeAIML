import streamlit as st
import requests

st.set_page_config(page_title="Legal Navigator", page_icon="⚖️")

st.title("⚖️ Simple Legal Navigator")
query = st.text_input("Enter your legal question:")

if st.button("Ask") and query:
    response = requests.post(
        "http://localhost:8000/ask",
        json={"query": query, "k": 5}
    )
    if response.status_code == 200:
        data = response.json()
        st.subheader("Answer")
        st.write(data["answer"])

        st.subheader("Relevant Documents")
        for ev in data["evidences"]:
            with st.expander(f"{ev['id']} (score: {ev['score']:.4f})"):
                st.write(ev["text"])
    else:
        st.error("Server error. Make sure FastAPI is running.")
