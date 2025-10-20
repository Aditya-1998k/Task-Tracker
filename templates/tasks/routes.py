"""
Adding All the routes for Tasks
1. Add task
2. Get task with IDs
3. Get all tasks
"""
from flask import Blueprint, request

from .task import get_tasks, add_task, get_task_by_user
from templates.auths.auth import role_required
from utilities.memcached_utils import get_cache
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

