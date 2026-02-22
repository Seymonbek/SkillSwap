from flask import Flask
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix


def create_app():
    app = Flask(__name__)

    # Configure CORS
    CORS(app)

    # Middleware for security headers
    app.wsgi_app = ProxyFix(app.wsgi_app)

    # Error Handlers
    @app.errorhandler(404)
    def not_found(e):
        return {'error': 'Not Found'}, 404

    @app.errorhandler(500)
    def internal_error(e):
        return {'error': 'Internal Server Error'}, 500

    return app
