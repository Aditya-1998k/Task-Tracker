"""
Adding All the routes for Tasks
1. Add task
2. Get task with IDs
3. Get all tasks
"""
from flask import Blueprint, request
from .task import get_tasks, add_task, get_task_with_id

task_blueprint = Blueprint('task', __name__)


@task_blueprint.route('/add_task', methods=['POST'])
def add_task_route():
    return add_task(request.json)

@task_blueprint.route('/tasks', methods=['GET'])
def get_tasks_route():
    return get_tasks()

@task_blueprint.route('/get_task', methods=['GET'])
def get_task_ids():
    data = request.get_json()
    task_id = data.get('_id')
    return get_task_with_id(task_id)
