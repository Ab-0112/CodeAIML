from flask import Blueprint
from flask_socketio import emit
from . import socketio

websocket2_bp = Blueprint('websocket2', __name__)

@socketio.on('connect', namespace='/notifications')
def handle_notifications_connect():
    emit('notification', {'data': 'Connected to notifications namespace'})

@socketio.on('disconnect', namespace='/notifications')
def handle_notifications_disconnect():
    print('Client disconnected from notifications namespace')

@socketio.on('notify', namespace='/notifications')
def handle_notify(data):
    notification = data.get('notification')
    emit('notification', {'data': notification}, broadcast=True)
