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
        description=data.get("description"),
        due_date=data.get("due_date")
    )

    task_id = tasks_collection.insert_one(task.to_dict()).inserted_id
    return jsonify({"message": "Task added", "task_id": str(task_id)})

def get_tasks():
    tasks = list(tasks_collection.find({}))
    for task in tasks:
        task["_id"] = str(task["_id"])
    return jsonify({"tasks": tasks})
