import os
import jwt
import logging
from functools import wraps
from datetime import datetime, timedelta
from flask import jsonify, request

# Local Imports
from utilities.logging_config import get_logger

logger = get_logger(__name__)


SECRET_KEY = os.environ.get('SECRET_KEY')
ALGORITHM = os.environ.get('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES')

def generate_token(data):
    """
    Using email, role and expiry time
    for token generation
    """
    try:
        payload = {
            "email": data.get('email'),
            "role": data.get('role'),
            "exp": datetime.utcnow() + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        logger.info(f"Token Generated successfully for user {data.get('email')}")
        return token
    except Exception as e:
        logger.exception(f"Failed to Generate token, Error:{e}")


def verify_token(token):
    """
    Authenticate the Token provided
    by the user
    """
    try:
        if token.startswith("Bearer "):
            token = token.split(" ")[1]
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError as e:
        logger.exception(f"Error while token verification, Error: {e}")
        return None
    except jwt.InvalidTokenError as e:
        logger.exception(f"Invalid Token, Error: {e}")
        return None
    except Exception as e:
        logger.exception(f"Token verification failed. Error: {e}")
        return None

def role_required(roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if request.role not in roles:
                logger.info(f"This request required {roles}, but user have {request.role}")
                return jsonify({"error": "Permission denied"}), 403
            return func(*args, **kwargs)
        return wrapper
    return decorator
