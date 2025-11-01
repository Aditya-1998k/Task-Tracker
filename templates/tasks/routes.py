"""
Adding All the routes for Tasks
1. Add task
2. Get task with IDs
3. Get all tasks
"""
from flask import Blueprint, request, jsonify

from .task import get_tasks, add_task, get_task_by_user
from templates.auths.auth import role_required
from templates.tasks.model import tasks_collection
from utilities.logging_config import get_logger


logger = get_logger(__name__)
task_blueprint = Blueprint('task', __name__)


@task_blueprint.route('/add_task', methods=['POST'])
@role_required(['admin'])
def add_task_route():
    return add_task(request.json)


@task_blueprint.route('/get_tasks', methods=['GET'])
def get_tasks_route():
    return get_tasks()


@task_blueprint.route('/get_my_task', methods=['GET'])
def get_user_tasks():
    username = request.username
    return get_task_by_user(username)


@task_blueprint.route("/status_summary")
def get_task_status_summary():
    pipeline = [
        {"$group": {"_id": "$status", "count": {"$sum": 1}}}
    ]
    result = list(tasks_collection.aggregate(pipeline))
    summary = {item["_id"]: item["count"] for item in result}

    return jsonify(summary)


@task_blueprint.route("/recent", methods=["GET"])
def get_recent_tasks():
    """
    Fetch the 10 most recent tasks from MongoDB.
    """
    try:
        # MongoDB query: sort by `created_at` descending (-1), limit 10
        recent_tasks = (
            tasks_collection.find({}, {"_id": 0})  # Exclude internal MongoDB _id if not needed
            .sort("created_at", -1)
            .limit(10)
        )

        tasks_list = list(recent_tasks)
        logger.critical(tasks_list)
        return jsonify({"tasks": tasks_list}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
