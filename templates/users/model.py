from app import mongo
from datetime import datetime
import bcrypt


user_collection = mongo.db.users

class Users:
    """Class User for mongodb"""
    def __init__(self, username, password, email, role, status):
        self.username = username
        self.password = self.generate_hash(password)
        self.email = email
        self.role = role
        self.status = "Y"
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        
    def generate_hash(self, password):
        """
        Generate a hash for the password
        bcrypt.gensalt() - Generate random byte string
        """
        salt = bcrypt.gensalt()
        encoded_password = password.encode('utf-8')
        return bcrypt.hashpw(encoded_password, salt)

    def to_dict(self):
        """
        Convert User object to a dictionary (for MongoDB)
        """
        return {
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "role": self.role,
            "status": self.status
        }