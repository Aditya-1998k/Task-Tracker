from flask import Blueprint, request
from flask import jsonify
from .user import get_users_session, add_user, get_all_users_data, get_user_data, change_user_password
from templates.auths.auth import role_required
from templates.auths.middleware import CACHE


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
    return users



@user_blueprint.route('/get_users', methods=['GET'])
@role_required(['admin'])
def get_all_users():
    users = get_all_users_data()
    if users:
        return jsonify({"users": users}), 200
    else:
        return jsonify({"message": "No users found"}), 404

@user_blueprint.route('/get_user', methods=['GET'])
def get_user():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"error": "Token is missing"}), 401
    email = CACHE.get(token).get('email')
    user_data = get_user_data(email)
    return jsonify({"user": user_data}), 200

@user_blueprint.route('/change_password', methods=['POST'])
def change_password():
    data = request.get_json()
    token = request.headers.get('Authorization')
    if not data and not token:
        return jsonify({"message": "No input data provided"}), 400

    email = CACHE.get(token).get('email')
    old_password = data.get('oldPassword')
    new_password = data.get('newPassword')
    return change_user_password(email, old_password, new_password)
