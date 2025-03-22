from flask import Blueprint
from flask_socketio import emit, join_room, leave_room
from . import socketio
from models.chat_ollama import ChatOllama

websocket1_bp = Blueprint('websocket1', __name__)
chat_model = ChatOllama(model_name='deepseek-r1:7b')

@socketio.on('connect', namespace='/chat')
def handle_connect():
    emit('message', {'data': 'Connected to chat namespace'})

@socketio.on('disconnect', namespace='/chat')
def handle_disconnect():
    print('Client disconnected from chat namespace')

@socketio.on('join', namespace='/chat')
def handle_join(data):
    room = data.get('room')
    join_room(room)
    emit('message', {'data': f'Joined room: {room}'}, room=room)

@socketio.on('leave', namespace='/chat')
def handle_leave(data):
    room = data.get('room')
    leave_room(room)
    emit('message', {'data': f'Left room: {room}'}, room=room)

@socketio.on('chat_message', namespace='/chat')
def handle_chat_message(data):
    room = data.get('room')
    message = data.get('message')
    response = chat_model.get_response(message)
    emit('chat_response', {'message': response}, room=room)
