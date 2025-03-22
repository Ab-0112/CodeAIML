from flask import Blueprint, request, jsonify
from models.chat_ollama import ChatOllama

route1_bp = Blueprint('route1', __name__)
chat_model = ChatOllama(model_name='deepseek-r1:7b')

@route1_bp.route('/api/response', methods=['POST'])
def get_response():
    data = request.get_json()
    prompt = data.get('prompt', '')
    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400
    response = chat_model.get_response(prompt)
    return jsonify({'response': response})
