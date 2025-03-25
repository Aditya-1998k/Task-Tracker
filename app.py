from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import urllib.parse
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


app = Flask(__name__)

# Construct the MongoDB URI using environment variables
MONGO_USER = urllib.parse.quote_plus(os.getenv("MONGO_USER"))
MONGO_PASSWORD = urllib.parse.quote_plus(os.getenv("MONGO_PASSWORD"))
MONGO_CLUSTER = os.getenv("MONGO_CLUSTER")
MONGO_DB = os.getenv("MONGO_DB")

MONGO_URI = f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_CLUSTER}/{MONGO_DB}?retryWrites=true&w=majority"
app.config["MONGO_URI"] = MONGO_URI

mongo = PyMongo(app)
tasks_collection = mongo.db.tasks

@app.route("/", methods=["GET"])
def welcome():
    return jsonify({"message": "Welcome to the Task Manager API!"})

@app.route("/add_task", methods=["POST"])
def add_task():
    data = request.json
    if not data or "task_name" not in data:
        return jsonify({"error": "Task name is required"}), 400
    
    task_id = tasks_collection.insert_one({"task_name": data["task_name"], "status": "pending"}).inserted_id
    return jsonify({"message": "Task added", "task_id": str(task_id)})

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = list(tasks_collection.find({}, {"_id": 0}))
    return jsonify({"tasks": tasks})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
