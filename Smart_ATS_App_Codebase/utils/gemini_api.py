import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-2.0-flash-thinking-exp')
    response = model.generate_content(prompt)
    return response.text
