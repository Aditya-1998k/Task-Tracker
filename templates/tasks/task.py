from flask import jsonify
from bson import ObjectId
from .model import Task, tasks_collection
from utilities.logging_config import get_logger

logger = get_logger(__name__)


def add_task(data):
    if not data or "summary" not in data:
        return jsonify({"error": "Task summary is required"}), 400
    
    task = Task(
        summary=data["summary"],
        task_type=data.get("task_type", "Development"),
        start_dt=data.get("start_dt"),
        status=data.get("status", "open"),
        estimate=data.get("estimate", 8),
        priority=data.get("priority", "medium"),
        assigned=data.get("assigned"),
        description=data.get("description"),
        due_date=data.get("due_date")
    )
    try:
        task_id = tasks_collection.insert_one(task.to_dict()).inserted_id
        return jsonify({"message": "Task added", "task_id": str(task_id)}), 200
    except Exception as e:
        return jsonify({"Error": f"Error while adding tasks. error: {e}"})


def get_tasks():
    """Add task to task collection"""
    tasks = list(tasks_collection.find({}))
    for task in tasks:
        task["_id"] = str(task["_id"])
    return jsonify({"tasks": tasks})


def get_task_by_user(username):
    """Fetch task with task id"""
    tasks = list(tasks_collection.find({"assigned": username}))
    if tasks:
        for task in tasks:
            task["_id"] = str(task["_id"])
        return jsonify({"tasks": tasks})
    else:
        return jsonify({"error": "Task not found"}), 404

