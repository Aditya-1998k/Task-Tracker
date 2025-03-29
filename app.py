from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from config import Config
from flask_cors import CORS
app = Flask(__name__)
app.config.from_object(Config)

CORS(app)

mongo = PyMongo(app)

from tasks.routes import task_blueprint
app.register_blueprint(task_blueprint, url_prefix="/tasks")

@app.route("/", methods=["GET"])
def welcome():
    return jsonify({"message": "Welcome to the Task Manager API!"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
