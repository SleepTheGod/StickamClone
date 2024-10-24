from app import socketio
from flask_socketio import emit, join_room, leave_room

@socketio.on('connect')
def handle_connect():
    emit('message', {'msg': 'User connected'})

@socketio.on('disconnect')
def handle_disconnect():
    emit('message', {'msg': 'User disconnected'})
