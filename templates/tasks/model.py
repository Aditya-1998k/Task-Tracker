from datetime import datetime
from app import mongo


tasks_collection = mongo.db.tasks

class Task:
    """ Task Model for MongoDB """
    def __init__(self, summary, task_type='Development', start_dt=None, status="pending", estimate=8, priority="medium", assigned=None, description=None, due_date=None):
        self.summary = summary
        self.task_type = task_type
        self.start_dt = start_dt
        self.status = status
        self.estimate = estimate
        self.priority = priority
        self.assigned = assigned
        self.description = description
        self.due_dt = due_date
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        Convert Task object to a dictionary (for MongoDB)
        """
        return {
            "summary": self.summary,
            "task_type": self.task_type,
            "start_dt": self.start_dt,
            "status": self.status,
            "estimate": self.estimate,
            "priority": self.priority,
            "assigned": self.assigned,
            "description": self.description,
            "due_date": self.due_dt,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
