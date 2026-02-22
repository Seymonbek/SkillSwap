from flask import request, make_response
from functools import wraps
from marshmallow import Schema, fields, ValidationError

# Rate Limiting Decorator
import time

class RateLimiter:
    def __init__(self, limit: int, per: int):
        self.limit = limit
        self.per = per
        self.users = {}  # stores timestamps of requests made by users

    def is_rate_limited(self, user_id: str):
        now = time.time()
        timestamps = self.users.get(user_id, [])
        self.users[user_id] = [t for t in timestamps if now - t < self.per]
        if len(self.users[user_id]) < self.limit:
            self.users[user_id].append(now)
            return False
        return True

rate_limiter = RateLimiter(limit=5, per=60)  # Limit to 5 requests per minute

# Input Validation Schema
class UserInputSchema(Schema):
    username = fields.String(required=True)
    email = fields.Email(required=True)

schema = UserInputSchema()

# Middleware to validate input
def validate_input(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        json_data = request.get_json() or {}
        try:
            schema.load(json_data)
        except ValidationError as err:
            return make_response({'error': err.messages}, 400)
        return func(*args, **kwargs)
    return decorated_function

# Middleware for Rate Limiting
def rate_limit(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        user_id = request.remote_addr  # Identify user by IP address
        if rate_limiter.is_rate_limited(user_id):
            return make_response({'error': 'Too many requests. Try again later.'}, 429)
        return func(*args, **kwargs)
    return decorated_function

# XSS Protection Middleware
def xss_protection(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        response = make_response(func(*args, **kwargs))
        response.headers['X-XSS-Protection'] = '1; mode=block'
        return response
    return decorated_function

# Security Headers Middleware
def security_headers(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        response = make_response(func(*args, **kwargs))
        response.headers['Content-Security-Policy'] = "default-src 'self'"  # Customize this as needed
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'DENY'
        return response
    return decorated_function

# Usage Example:
# @app.route('/some_route', methods=['POST'])
# @validate_input
# @rate_limit
# @xss_protection
# @security_headers
# def some_route():
#     return make_response({'message': 'Success!'}, 200)