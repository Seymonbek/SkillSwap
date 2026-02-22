from flask import Blueprint, request, jsonify

# Create a Blueprint for session routes
sessions_bp = Blueprint('sessions', __name__)

# In-memory storage for sessions (for example purposes)
sessions = {}
next_id = 1

# POST /sessions
@sessions_bp.route('/sessions', methods=['POST'])
def create_session():
    global next_id
    session_data = request.json
    session_id = next_id
    sessions[session_id] = {
        'id': session_id,
        'data': session_data,
        'status': 'inactive',
    }
    next_id += 1
    return jsonify(sessions[session_id]), 201

# PATCH /sessions/<id>/start
@sessions_bp.route('/sessions/<int:id>/start', methods=['PATCH'])
def start_session(id):
    if id in sessions:
        sessions[id]['status'] = 'active'
        return jsonify(sessions[id]), 200
    return jsonify({'error': 'Session not found'}), 404

# PATCH /sessions/<id>/end
@sessions_bp.route('/sessions/<int:id>/end', methods=['PATCH'])
def end_session(id):
    if id in sessions:
        sessions[id]['status'] = 'ended'
        return jsonify(sessions[id]), 200
    return jsonify({'error': 'Session not found'}), 404

# GET /sessions
@sessions_bp.route('/sessions', methods=['GET'])
def get_sessions():
    return jsonify(list(sessions.values())), 200
