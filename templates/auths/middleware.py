import os
from flask import request, jsonify
from .auth import verify_token

# Route That don't require Auth
PUBLIC_ENDPOINTS = {
    'user.login',
    'user.signup'
}

AUTH_ENABLED = os.getenv('AUTH_ENABLED')

def auth_middleware(app):
    @app.before_request
    def before_request():
        if not AUTH_ENABLED:
            return None
        
        if request.endpoint in PUBLIC_ENDPOINTS:
            return None
        
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"error": "Token is missing"}), 401

        try:
            payload = verify_token(token)
            request.email = payload.get('email')
            request.role = payload.get('role')
        except Exception as e:
            return jsonify({"error": str(e)}), 401
