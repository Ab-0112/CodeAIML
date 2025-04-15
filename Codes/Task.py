import logging
import time
import subprocess
import re
import json
from flask import Flask
from flask_socketio import SocketIO, emit
from langchain.prompts import ChatPromptTemplate
from langchain_ollama.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel, ValidationError
from typing import List, Optional

# =========================== GLOBAL VARIABLES =========================== #
OLLAMA_MODEL_NAME = "gemma3:1b"
vector_db = None
task_chain = None
DB_DIRECTORY = "chroma_db"

# =========================== INITIALIZE FLASK AND SOCKET.IO =========================== #
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet", ping_timeout=300, ping_interval=30)

logging.basicConfig(level=logging.INFO)

# =========================== PYDANTIC MODELS =========================== #
class Task(BaseModel):
    task_title: str
    scenario_context: str
    objective: str
    task_description: str
    resources: List[str]
    estimated_time: int
    evaluation_criteria: str
    additional_considerations: Optional[str] = None
    follow_up_tasks: Optional[List[str]] = None

class TaskOutput(BaseModel):
    tasks: List[Task]

# =========================== UTILITY FUNCTIONS =========================== #
def ensure_model_available(model_name):
    """Ensure the Ollama model is available by pulling it if necessary."""
    try:
        logging.info(f"🔍 Checking model availability: {model_name}")
        subprocess.run(["ollama", "pull", model_name], check=True)
        logging.info(f"✅ Model '{model_name}' is ready.")
    except subprocess.CalledProcessError:
        logging.error(f"🚨 Failed to pull model '{model_name}'. Ensure Ollama is running.")
        raise RuntimeError(f"Model '{model_name}' not available. Please start Ollama.")

def extract_json(text):
    """Extracts only the JSON content from a given text."""
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(0))  # Ensure valid JSON parsing
        except json.JSONDecodeError:
            return None
    return None

# =========================== TASK CHAIN INITIALIZATION =========================== #
def initialize_task_chain():
    """Initialize the task generation chain using the Ollama model."""
    global vector_db, task_chain

    ensure_model_available(OLLAMA_MODEL_NAME)  # Ensure embeddings model is available

    task_prompt = ChatPromptTemplate.from_template(
    """
Create six realistic, scenario-based interview tasks to effectively evaluate a candidate's ability to perform job-specific duties.

Each task should align with the job title, required skills, complexity level, and company context, ensuring it is practical and measurable.

🔹 Input Parameters:
Job Title: {job_title}
Key Competencies: {competencies}
Task Duration (minutes): {duration}
Complexity Level: {complexity}
Job Description: {job_description}
Company Name: {company_name}
Company Description: {company_description}
🔹 Task Design Guidelines:
✅ Each task must be practical, relevant, and scenario-based.
✅ Reflect real-world challenges that the candidate would encounter in this role.
✅ Maintain a logical sequence, with some tasks allowing for follow-up discussions or refinements.
✅ Specify relevant tools, technologies, or resources where applicable.
✅ Ensure the evaluation criteria are specific, measurable, and job-relevant.

🔹 STRICT JSON OUTPUT FORMAT:
Return a valid JSON object containing exactly six interview tasks, following this structure:
    {{
        "tasks": [
            {{
                "task_title": "Task 1 Title",
                "scenario_context": "Brief, realistic scenario setting the stage for Task 1.",
                "objective": "Clearly state what this task assesses (e.g., problem-solving, technical proficiency).",
                "task_description": "Detailed instructions on what the candidate must do.",
                "resources": ["List of relevant tools, platforms, or datasets needed."],
                "estimated_time": 30,
                "evaluation_criteria": "Define key success factors (e.g., accuracy, efficiency, innovation).",
                "additional_considerations": "Any optional aspects (e.g., time constraints, bonus challenges).",
                "follow_up_tasks": ["Optional follow-up questions to explore deeper insights."]
            }}
        ]
    }}

    🔹 FINAL INSTRUCTIONS:
✅ Return only a valid JSON object. No explanations or extra text.
✅ Ensure exactly SIX well-structured tasks are generated.
✅ Tasks should be role-specific, measurable, and practical.
    """
)

    task_chain = task_prompt | ChatOllama(model=OLLAMA_MODEL_NAME, streaming=True) | StrOutputParser()
    return True

# =========================== SOCKET.IO EVENTS =========================== #
@socketio.on('generate_task')
def handle_generate_task(json_data):
    """Handles task generation based on client input and sends structured JSON output."""
    try:
        logging.info(f"📥 Received JSON Data: {json_data}")  

        if isinstance(json_data, str):
            json_data = json.loads(json_data)

        job_title = json_data.get("jobTitle") or json_data.get("job_title", "").strip()
        competencies = json_data.get("competencies") or json_data.get("skills_required", [])
        description = json_data.get("description") or ", ".join(json_data.get("roles_and_responsibilities", []))
        duration = json_data.get("duration", 60)
        complexity = json_data.get("complexity", "Medium")

        company = json_data.get("company", {})
        company_name = company.get("name", "").strip()
        company_description = company.get("description", "").strip()

        logging.info(f"📌 Extracted Data - Job Title: {job_title}, Description: {description}, Company Name: {company_name}")

        if not job_title or not description or not company_name:
            logging.error("🚨 Required fields are missing! Check the request payload.")
            emit('message', {'data': '❌ Required fields are missing!'})
            return

        if task_chain is None:
            logging.error("🚨 Task chain is not initialized!")
            emit('message', {'data': '❌ Task chain is not initialized!'})
            return

        logging.info(f"⚡ Generating tasks for job title: {job_title}")
        start_time = time.time()

        response_generator = task_chain.stream({
            "job_title": job_title,
            "competencies": competencies,
            "duration": duration,
            "complexity": complexity,
            "job_description": description,
            "company_name": company_name,
            "company_description": company_description
        })

        response_data = ""

        for chunk in response_generator:
            logging.info(f"🧩 Chunk received: {chunk.strip()}")
            response_data += chunk

        if not response_data.strip():
            logging.error("❌ Error: Received empty response from AI model.")
            emit('message', {'data': "❌ Error: Received empty response from AI model."}, broadcast=True)
            return
        logging.info(f"📤 Final response: {response_data}")
        extracted_json = extract_json(response_data)

        if extracted_json:
            logging.info(f"✅ Extracted JSON: {extracted_json}")
        else:
            logging.error("❌ No valid JSON found!")

        try:
            task_output = TaskOutput(**extracted_json)

            emit('task_output', {'tasks': task_output.model_dump()}, broadcast=True)
            elapsed_time = time.time() - start_time
            logging.info(f"✅ Task generation completed in {elapsed_time:.2f} seconds.")
            emit('task_completion', {'elapsed_time': elapsed_time}, broadcast=True)

        except ValidationError as e:
            logging.error(f"❌ Validation Error: {str(e)}")
            emit('message', {'data': f"Validation Error: {e.errors()}"}, broadcast=True)

    except Exception as e:
        logging.error(f"🚨 Error during task generation: {e}")
        emit('message', {'data': f"❌ Error: {str(e)}"}, broadcast=True)

# Server start
if __name__ == '__main__':
    logging.info("⚡ Starting WebSocket server...")

    if initialize_task_chain():
        logging.info("✅ Task chain initialized!")
    else:
        logging.error("🚨 Failed to initialize task chain!")

    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
  