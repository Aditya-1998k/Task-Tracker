from flask import Blueprint, request
from .task import get_tasks, add_task
from flask import jsonify

task_blueprint = Blueprint('task', __name__)

@task_blueprint.route('/welcome', methods=['GET'])
def welcome():
    return jsonify({"message": "Welcome to the Task Manager API!"})

@task_blueprint.route('/add_task', methods=['POST'])
def add_task_route():
    return add_task(request.json)

@task_blueprint.route('/get_tasks', methods=['GET'])
def get_tasks_route():
    return get_tasks()
