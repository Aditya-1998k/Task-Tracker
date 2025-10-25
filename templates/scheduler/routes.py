from flask import Blueprint, request, jsonify
import uuid
from dateutil import parser
from pytz import UTC
from datetime import datetime, timedelta

from utilities.scheduler import send_alert_job
from app import scheduler
from apscheduler.triggers.cron import CronTrigger
from utilities.logging_config import get_logger

logger = get_logger(__name__)

scheduler_blueprint = Blueprint('scheduler', __name__)

@scheduler_blueprint.route("/scheduler_alert", methods=['POST'])
def schedule_alert():
    data = request.get_json()
    schedule_type = data.get("type", "once")
    job_id = str(uuid.uuid4())
    if scheduler.running:
        logger.info("[Scheduler] ✅ Scheduler is running")
    else:
        logger.critical("[Scheduler] ❌ Scheduler not started")

    if schedule_type == "daily":
        scheduler.add_job(
            send_alert_job,
            id=job_id,
            trigger=CronTrigger(hour=9, minute=0),
            replace_existing=True,
        )
    elif schedule_type == "once":
        run_time_str = data.get("run_at")
        run_time = parser.isoparse(run_time_str)
        if run_time.tzinfo is None:
            run_time = run_time.replace(tzinfo=UTC)
        scheduler.add_job(
            send_alert_job,
            id=job_id,
            trigger='date',
            run_date=run_time,
            replace_existing=True,
        )
    elif schedule_type == "now":
        scheduler.add_job(
        send_alert_job,
            id="test_job",
            trigger='date',
            run_date=datetime.utcnow() + timedelta(seconds=10),
        )
    else:
        return {"error": "Invalid schedule type. Use 'daily' or 'once'."}, 400

    return {"message": "Job scheduled successfully", "job_id": job_id}, 200


@scheduler_blueprint.route("/scheduler_jobs", methods=["GET"])
def list_jobs():
    jobs = scheduler.get_jobs()
    job_list = []
    for job in jobs:
        # Safely get next_run_time
        next_run = getattr(job, "next_run_time", None)
        if next_run:
            next_run = next_run.isoformat()
        job_list.append({
            "id": getattr(job, "id", None),
            "next_run_time": next_run,
            "trigger": str(getattr(job, "trigger", None))
        })
    return jsonify(job_list)

