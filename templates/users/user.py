import bcrypt
from .model import user_collection
from .model import Users
from templates.auths.auth import generate_token
from flask import jsonify
from flask import jsonify
from utilities.rmq_utils import publish_to_rabbimq


def get_users_session(data):
    email = data.get("email")
    password = data.get("password")
    user_data = user_collection.find_one({"email": email})

    if bcrypt.checkpw(password.encode("utf-8"), user_data["password"]):
        token = generate_token(user_data)
        return token


def add_user(data):
    if (
        not data
        or "username" not in data
        or "password" not in data
        or "email" not in data
    ):
        return None

    user_data = user_collection.find_one({"email": data["email"]})
    if user_data:
        return jsonify({"error": "user already Exists"}), 400

    user = Users(
        username=data["username"],
        password=data["password"],
        email=data["email"],
        role=data.get("role", "user"),
        status=data.get("status", "Y"),
    )
    user_collection.insert_one(user.to_dict())

    # Publish message to welcome service
    publish_to_rabbimq(queue="welcome", payload=data["email"])

    return jsonify({"message": "User added successfully"}), 201


def get_all_users_data():
    result = []
    users = list(user_collection.find({}))
    for user in users:
        result.append(
            {
                "username": user.get("username"),
                "email": user.get("email"),
                "role": user.get("role"),
                "status": user.get("status"),
            }
        )
    return result


def get_user_data(email):
    user = user_collection.find_one({"email": email})
    if user:
        return {
            "username": user.get("username"),
            "email": user.get("email"),
            "role": user.get("role"),
            "status": user.get("status"),
        }
    else:
        return None


def change_user_password(email, old_password, new_password):
    user = user_collection.find_one({"email": email})
    if user:
        if bcrypt.checkpw(old_password.encode("utf-8"), user["password"]):
            user_collection.update_one(
                {"email": email},
                {
                    "$set": {
                        "password": bcrypt.hashpw(
                            new_password.encode("utf-8"), bcrypt.gensalt()
                        )
                    }
                },
            )
            return jsonify({"message": "Password changed successfully"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401
