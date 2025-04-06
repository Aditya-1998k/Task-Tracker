from flask import Blueprint, request
from flask import jsonify
from .user import get_users_session, add_user

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"message": "No input data provided"}), 400

    token = get_users_session(data)
    if token:
        return jsonify({"token": token}), 200
    else:
        return jsonify({"Error": "Login failed"}), 401


@user_blueprint.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    if not data:
        return jsonify({"message": "No input data provided"}), 400
    users = add_user(data)

    if users:
        return jsonify({"message": "User signup successsfully"}), 201
    else:
        return jsonify({"message": "Signup failed"}), 400
