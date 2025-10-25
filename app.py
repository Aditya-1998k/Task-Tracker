# app.py
from flask import Flask, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from utilities.rmq_utils import publish_to_rabbimq
from templates.auths.middleware import auth_middleware

# Import Config
from config import Config


scheduler = BackgroundScheduler()


# Scheduler

app = Flask(__name__)
auth_middleware(app)
app.config.from_object(Config)
CORS(app)
mongo = PyMongo(app)


from templates.tasks.routes import task_blueprint
from templates.users.routes import user_blueprint
from templates.scheduler.routes import scheduler_blueprint

# Register blueprints
app.register_blueprint(task_blueprint, url_prefix="/tasks")
app.register_blueprint(user_blueprint, url_prefix="/users")
app.register_blueprint(scheduler_blueprint, url_prefix="/scheduler")


# Root route
@app.route("/", methods=["GET"])
def welcome():
    return jsonify({"message": "Welcome to the Task Tracker !"})


def start_scheduler():
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown(wait=False))
    print("[Scheduler] Started successfully")

start_scheduler()

# Run app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)

