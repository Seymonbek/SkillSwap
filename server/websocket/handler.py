from flask import Flask
from flask_socketio import SocketIO, emit
import time

app = Flask(__name__)
socketio = SocketIO(app)

# Set to track connected users
connected_users = set()

# Heartbeat mechanism
@socketio.on('heartbeat')
def handle_heartbeat():
    emit('heartbeat', {'status': 'alive'}, broadcast=True)  # Respond back to all clients

# User presence tracking
@socketio.on('connect')
def handle_connect():
    user_id = request.args.get('user_id')
    if user_id:
        connected_users.add(user_id)
        emit('user_status', {'users': list(connected_users)}, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    user_id = request.args.get('user_id')
    if user_id:
        connected_users.discard(user_id)
        emit('user_status', {'users': list(connected_users)}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)