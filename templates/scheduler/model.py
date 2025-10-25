from datetime import datetime



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

