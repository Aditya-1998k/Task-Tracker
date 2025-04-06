from flask import jsonify
from bson import ObjectId
from .model import Task, tasks_collection


def add_task(data):
    if not data or "summary" not in data:
        return jsonify({"error": "Task summary is required"}), 400
    
    task = Task(
        summary=data["summary"],
        task_type=data.get("task_type", "task"),
        start_dt=data.get("start_dt"),
        status=data.get("status", "pending"),
        estimate=data.get("estimate", 8),
        priority=data.get("priority", "medium"),
        assigned=data.get("assigned"),
        description=data.get("description"),
        due_date=data.get("due_date")
    )

    task_id = tasks_collection.insert_one(task.to_dict()).inserted_id
    return jsonify({"message": "Task added", "task_id": str(task_id)})


def get_tasks():
    """Add task to task collection"""
    tasks = list(tasks_collection.find({}))
    for task in tasks:
        task["_id"] = str(task["_id"])
    return jsonify({"tasks": tasks})


def get_task_with_id(task_id):
    """Fetch task with task id"""
    task = tasks_collection.find_one({"_id": ObjectId(task_id)})
    if task:
        task["_id"] = str(task["_id"])
        return jsonify({"task": task})
    else:
        return jsonify({"error": "Task not found"}), 404
