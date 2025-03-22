from flask import Blueprint, request, jsonify
from models.chat_ollama import ChatOllama

route2_bp = Blueprint('route2', __name__)
chat_model = ChatOllama(model_name='deepseek-r1:7b')

@route2_bp.route('/api/summary', methods=['POST'])
def get_summary():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'Text is required'}), 400
    prompt = f"Summarize the following text: {text}"
    summary = chat_model.get_response(prompt)
    return jsonify({'summary': summary})
