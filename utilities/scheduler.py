from datetime import datetime
import atexit
from apscheduler.schedulers.background import BackgroundScheduler

from utilities.rmq_utils import publish_to_rabbimq


scheduler = BackgroundScheduler()

def start_scheduler():
    if not scheduler.running:
        scheduler.start()
        atexit.register(lambda: scheduler.shutdown(wait=False))
        print("[Scheduler] Started successfully")


def send_alert_job():
    try:
        payload = {
            "event": "SEND_ALERT",
            "timestamp": datetime.utcnow().isoformat()
        }
        publish_to_rabbimq('alert_user', payload)
        print(f"[{datetime.now()}] ✅ Published message to alert user for pending tasks.")
    except Exception as e:
        print(f"[{datetime.now()}] ❌ Failed to send alert: {e}")


