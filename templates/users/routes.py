from flask import Blueprint, request
from flask import jsonify
from .user import (
    forget_password, 
    get_users_session, 
    add_user, 
    get_all_users_data, 
    get_user_data, 
    change_user_password,
)
from templates.auths.auth import role_required

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/login', methods=['POST'])
def login():
    """
    Payload:
        {
            "password": "S3cureP@ssw0rd",
            "email": "alice@example.com"
        }
    returns:
        Generated Tokens
    """
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
    """
    Arguments:
    {
        username : username,
        password : password,
        email : email.
        role : (developer or admin or user),
        status : optional ('Y')
    }
    Return: User Data
    """
    data = request.get_json()
    if not data:
        return jsonify({"message": "No input data provided"}), 400
    return add_user(data)


@user_blueprint.route('/get_users', methods=['GET'])
@role_required(['admin'])
def get_all_users():
    users = get_all_users_data()
    if users:
        return jsonify({"users": users}), 200
    else:
        return jsonify({"message": "No users found"}), 404


@user_blueprint.route('/get_user', methods=['GET'])
@role_required(['admin'])
def get_user():
    """
    payload : {"email": "example@gmail.com"}
    """
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"error": "Token is missing"}), 401

    data = request.get_json()
    email = data.get('email')
    user_data = get_user_data(email)
    return jsonify({"user": user_data}), 200


@user_blueprint.route('/change_password', methods=['POST'])
def change_password():
    """
    Payload:
    {
        "email": "test@gmail.com",
        "old_password": "secret_old",
        "new_password": "secret_new"
    }
    """
    data = request.get_json()
    email = data.get('email')
    old_password = data.get('oldPassword')
    new_password = data.get('newPassword')
    return change_user_password(email, old_password, new_password)


@user_blueprint.route('/forget_password', methods=['POST'])
def forget_user_password():
    """
    Payload:
    {
        "email": "test@gmail.com"    
    }
    """
    data = request.get_json()
    email = data.get('email')
    return forget_password(email)

