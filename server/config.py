import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'your_jwt_secret'

    # Production settings
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    # Any other production settings can go here
