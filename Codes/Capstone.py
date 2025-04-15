import logging
import time
import subprocess
import re
import json
from flask import Flask, request, Response, jsonify, stream_with_context
from langchain.prompts import ChatPromptTemplate
from langchain_ollama.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel, ValidationError
from typing import List

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

capstone_chain = None

# =========================== SCHEMA =========================== #
class CapstoneModule(BaseModel):
    name: str
    description: str
    content_type: str
    content_duration: str

class CapstonePhase(BaseModel):
    name: str
    duration: str
    modules: List[CapstoneModule]

class CapstoneProject(BaseModel):
    title: str
    description: str
    technologies: List[str]
    expected_outcomes: List[str]
    deliverables: List[str]
    phases: List[CapstonePhase]

# =========================== UTILS =========================== #
def ensure_model_available(model_name: str):
    try:
        subprocess.run(["ollama", "pull", model_name], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        logging.info(f"✅ Model '{model_name}' is ready.")
    except subprocess.CalledProcessError:
        logging.error(f"🚨 Failed to pull model '{model_name}'. Ensure Ollama is running.")
        raise RuntimeError(f"🚨 Failed to pull model '{model_name}'.")

def extract_json(text: str) -> dict:
    try:
        match = re.search(r'\{.*\}', text, re.DOTALL)
        if match:
            cleaned = re.sub(r'[“”]', '"', match.group(0))
            cleaned = re.sub(r"’", "'", cleaned)
            cleaned = re.sub(r"```json", "", cleaned)
            cleaned = re.sub(r"```", "", cleaned)
            return json.loads(cleaned)
        else:
            logging.error("❌ No JSON object found.")
            return None
    except json.JSONDecodeError as e:
        logging.error(f"❌ JSON decode error: {e}")
        return None

# =========================== CHAIN INIT =========================== #
def initialize_capstone_generator():
    global capstone_chain

    ensure_model_available("gemma3:1b")

    capstone_prompt = ChatPromptTemplate.from_template(
        """
        Learning Path:
        {LEARNING_PATH}

        Generate a Capstone Project in this **strict JSON** format:

        {{
            "title": "Project Title",
            "description": "Overview of the project",
            "technologies": ["Tech 1", "Tech 2", "..."],
            "expected_outcomes": ["Outcome 1", "Outcome 2"],
            "deliverables": ["Deliverable 1", "Deliverable 2"],
            "phases": [
                {{
                    "name": "Phase Name",
                    "duration": "e.g. 2 weeks",
                    "modules": ["Module 1", "Module 2"]
                }}
            ]
        }}

        ❗ Only return a single valid JSON object. No extra commentary.
        """
    )

    capstone_chain = capstone_prompt | ChatOllama(model="gemma3:1b", streaming=True) | StrOutputParser()
    logging.info("✅ Capstone generator initialized.")

# =========================== STREAMING ROUTE =========================== #
@app.route('/generate_project', methods=['POST'])
def generate_project():
    if capstone_chain is None:
        return jsonify({'message': '❌ Capstone generator not initialized!'}), 500

    data = request.get_json()
    if not data:
        return jsonify({'message': '❌ No JSON data provided!'}), 400

    learning_path = data.get("learning_path")
    if not learning_path:
        return jsonify({'message': '❌ Missing \"learning_path\" in request!'}), 400

    if isinstance(learning_path, dict):
        learning_path = json.dumps(learning_path, indent=2)

    logging.info("🎯 Starting capstone generation stream...")

    def stream_response():
        sentence_buffer = ""
        full_response = ""
        try:
            for chunk in capstone_chain.stream({"LEARNING_PATH": learning_path}):
                full_response += chunk
                sentence_buffer += chunk

                # Stream complete sentences
                sentences = re.split(r'(?<=[.!?])\s+', sentence_buffer)
                for sentence in sentences[:-1]:
                    yield f"{sentence.strip()}\n"
                sentence_buffer = sentences[-1]

            if sentence_buffer.strip():
                yield f"{sentence_buffer.strip()}\n"

            # Extract and yield validated JSON block
            parsed_json = extract_json(full_response)
            if parsed_json:
                project = CapstoneProject(**parsed_json)
                yield "\n---\n"
                yield json.dumps(project.model_dump(), indent=2) + "\n"
            else:
                yield "\n❌ Failed to extract structured project.\n"

        except ValidationError as e:
            yield f"\n❌ Validation Error:\n{e}\n"
        except Exception as e:
            logging.error(f"🚨 Streaming error: {e}")
            yield f"\n❌ Error: {str(e)}\n"

    return Response(stream_with_context(stream_response()), content_type="text/plain")

# =========================== ENTRYPOINT =========================== #
if __name__ == '__main__':
    logging.info("🚀 Starting Flask server...")
    initialize_capstone_generator()
    app.run(host='0.0.0.0', port=5000, debug=True)
