import bcrypt
from .model import user_collection
from .model import Users
from templates.auths.auth import generate_token
from flask import jsonify
from flask import jsonify


def get_users_session(data):
    email = data.get('email')
    password = data.get('password')
    user_data = user_collection.find_one({"email": email})

    if bcrypt.checkpw(password.encode('utf-8'), user_data['password']):
        token = generate_token(user_data)
        return token


def add_user(data):
    if not data or "username" not in data or "password" not in data or "email" not in data:
        return None
    
    user_data = user_collection.find_one({"email": data['email']})
    if user_data:
        return jsonify({"error": "user already Exists"}), 400

    user = Users(
        username=data['username'],
        password=data['password'],
        email=data['email'],
        role=data.get('role', 'user'),
        status=data.get('status', 'Y')
    )
    user_collection.insert_one(user.to_dict())
    return jsonify({"message": "User added successfully"}), 201


def get_all_users_data():
    result = []
    users = list(user_collection.find({}))
    for user in users:
        result.append({
            "username": user.get("username"),
            "email": user.get("email"),
            "role": user.get("role"),
            "status": user.get("status")
        })
    return result
