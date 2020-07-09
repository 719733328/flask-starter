from flask_socketio import SocketIO, emit
from app.extensions import socketio


@socketio.on('my event')
def test_message(message):
    emit('my response', {'data': 'got it!'})
