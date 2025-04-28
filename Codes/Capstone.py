import logging
import subprocess
import re
import json
from flask import Flask, request, jsonify
from flask_cors import CORS  # Importing CORS from flask_cors
from langchain.prompts import ChatPromptTemplate
from langchain_ollama.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel, ValidationError
from typing import List

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes (you can restrict this to specific origins if needed)

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

    try:
        ensure_model_available("gemma3:1b")
    except RuntimeError as e:
        logging.error("🚨 Capstone generator initialization failed.")
        return

    capstone_prompt = ChatPromptTemplate.from_template(
    """
    Learning Path Description:
    {LEARNING_PATH}

    Generate a detailed Capstone Project plan that includes:
    1. A creative title
    2. Clear project objectives
    3. Relevant technologies
    4. Expected outcomes
    5. Key deliverables
    6. Phased implementation plan

    Structure your final answer in this exact JSON format:
    {{
        "title": "Project Title",
        "description": "Project overview...",
        "technologies": ["Tech 1", "Tech 2"],
        "expected_outcomes": ["Outcome 1", "Outcome 2"],
        "deliverables": ["Deliverable 1", "Deliverable 2"],
        "phases": [
            {{
                "name": "Phase Name",
                "duration": "X weeks",
                "modules": [
                    {{
                        "name": "Module Name",
                        "description": "Module purpose...",
                        "content_type": "Type",
                        "content_duration": "X hours"
                    }}
                ]
            }}
        ]
    }}
    """
)

    capstone_chain = capstone_prompt | ChatOllama(model="gemma3:1b", streaming=True) | StrOutputParser()
    logging.info("✅ Capstone generator initialized.")

# =========================== ROUTE TO GENERATE PROJECT =========================== #
@app.route('/generate_project', methods=['POST'])
def generate_project():
    if capstone_chain is None:
        return jsonify({'error': 'Generator not initialized'}), 500

    try:
        data = request.get_json()
        if not data or 'learning_path' not in data:
            return jsonify({'error': 'Missing learning_path'}), 400

        learning_path = data['learning_path']

        # Generate project raw output from model
        full_response = capstone_chain.invoke({
            "LEARNING_PATH": json.dumps(learning_path, indent=2)
        })

        # Log raw output for debugging
        logging.info("Raw model output:\n" + full_response)

        # Optionally, return raw output directly (for debugging)
        # return jsonify({'raw_output': full_response})

        # Extract JSON from raw output
        project_json = extract_json(full_response)
        if not project_json:
            return jsonify({'error': 'Failed to generate valid project structure'}), 500

        # Validate and return structured project
        project = CapstoneProject(**project_json)
        return jsonify({
            'title': project.title,
            'description': project.description,
            'technologies': project.technologies,
            'expected_outcomes': project.expected_outcomes,
            'deliverables': project.deliverables,
            'phases': [phase.dict() for phase in project.phases]
        })

    except ValidationError as e:
        logging.error(f"Validation error: {e}")
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

# =========================== ENTRYPOINT =========================== #
if __name__ == '__main__':
    logging.info("🚀 Starting Flask server...")
    initialize_capstone_generator()
    app.run(host='0.0.0.0', port=8080, debug=True)
