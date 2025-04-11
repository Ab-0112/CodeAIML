import streamlit as st
import time

def stream_text(text):
    for line in text.split("\n"):
        st.write(line)
        time.sleep(0.1)
