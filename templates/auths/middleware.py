import os
from flask import request, jsonify
from .auth import verify_token
from utilities.memcached_utils import set_cache
from utilities.logging_config import get_logger

logger = get_logger(__name__)
# Route That don't require Auth
PUBLIC_ENDPOINTS = {
    "user.login",
    "user.signup",
    "welcome",
    "user.change_password",
    "user.forget_user_password"
}


expire_time = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")
AUTH_ENABLED = os.getenv("AUTH_ENABLED")


def auth_middleware(app):
    @app.before_request
    def before_request():
        if request.method == "OPTIONS":
            return "", 200
        if not AUTH_ENABLED:
            return None
        logger.critical(f"Skipping auth for public endpoint: {request.endpoint}")

        if request.endpoint in PUBLIC_ENDPOINTS:
            return None

        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"error": "Token is missing"}), 401

        try:
            payload = verify_token(token)
            if not payload:
                return jsonify({"Error": "Invalid Token"})
            logger.info(f"Debugging: {payload}")
            request.email = payload.get("email")
            request.role = payload.get("role")
            request.username = payload.get("username")
            print(request.username)
            set_cache(token, payload, int(expire_time) * 60)
        except Exception as e:
            return jsonify({"error": str(e)}), 401
