import os
import urllib.parse
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for Flask app."""
    
    MONGO_USER = urllib.parse.quote_plus(os.getenv("MONGO_USER", "default_user"))
    MONGO_PASSWORD = urllib.parse.quote_plus(os.getenv("MONGO_PASSWORD", "default_password"))
    MONGO_CLUSTER = os.getenv("MONGO_CLUSTER", "your-default-cluster.mongodb.net")
    MONGO_DB = os.getenv("MONGO_DB", "task_tracker_db")

    MONGO_URI = f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_CLUSTER}/{MONGO_DB}?retryWrites=true&w=majority"

