from flask import Flask, jsonify
from flask_pymongo import PyMongo
from config import Config
from flask_cors import CORS
from templates.auths.middleware import auth_middleware


app = Flask(__name__)
auth_middleware(app)
app.config.from_object(Config)
CORS(app)
mongo = PyMongo(app)

## Import templates
from templates.tasks.routes import task_blueprint
from templates.users.routes import user_blueprint

## Register Blueprint
app.register_blueprint(task_blueprint, url_prefix="/tasks")
app.register_blueprint(user_blueprint, url_prefix="/users")


@app.route("/", methods=["GET"])
def welcome():
    return jsonify({"message": "Welcome to the Task Manager API!"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
