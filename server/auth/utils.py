import bcrypt
import jwt
from functools import wraps
from flask import request, jsonify, current_app

# Password hashing

def hash_password(password):
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed

# JWT token generation

def generate_token(user_id):
    token = jwt.encode({'user_id': user_id}, current_app.config['SECRET_KEY'], algorithm='HS256')
    return token

# JWT token verification

def verify_token(token):
    try:
        payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

# Authentication decorator

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        user_id = verify_token(token)
        if not user_id:
            return jsonify({'message': 'Token is invalid!'}), 403
        return f(user_id, *args, **kwargs)
    return decorated
