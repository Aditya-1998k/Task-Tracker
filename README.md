## Project Description
The **Task Tracker Backend** is a RESTful API built using **Flask** to manage tasks efficiently. It provides user authentication, task creation, updates, and tracking functionalities. Designed for scalability, supports integration with **SQL/NoSQL databases**.

Deployment URL : https://task-tracker-backend-yv45.onrender.com

### Key Features  
✅ **User authentication & authorization (JWT-based)**  
✅ **CRUD operations for tasks** (Create, Read, Update, Delete)  
✅ **Task status updates & deadlines tracking**  
✅ **Database support** (PostgreSQL/MongoDB)  
✅ **Asynchronous task processing** using Celery & RabbitMQ (optional)  
✅ **Dockerized for easy deployment**  

### Tech Stack  
- **Backend:** Flask, Flask-RESTful, SQLAlchemy  
- **Database:** PostgreSQL / MongoDB  
- **Authentication:** JWT  
- **Containerization:** Docker  

### Steps to Start the APP
1. create a virtual Environment
```
python3 -m venv backend
source backend/bin/activate
```
2. Install Dependency
```
pip install -r requirements.txt
```
3. create .env file and place following details
```
MONGO_USER="dummyuser"
MONGO_PASSWORD="dummypassword"
MONGO_CLUSTER="dummy-tracker-abcd.mongodb.net"
MONGO_DB="task-tracker"
SECRET_KEY="alpha"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES="10"
AUTH_ENABLE=True
```
4. Run the flask App
```
flask run --host=0.0.0.0 --port=5001 --reload
```
5. Stop the server (CLTRL + C)
6. Deactivate the virtual environment
```
deactivate
```


##  Endpoints Overview

| Endpoint                   | Method | Description                                      |
|----------------------------|--------|--------------------------------------------------|
| `/register`                | POST   | Register a new user                             |
| `/login`                   | POST   | Authenticate and obtain a JWT token             |
| `/tasks`                   | GET    | Get all tasks for the authenticated user         |
| `/tasks`                   | POST   | Create a new task                                |
| `/tasks/<task_id>`         | PUT    | Update a specific task                           |
| `/tasks/<task_id>`         | DELETE | Delete a specific task                           |
| `/tasks/<task_id>/status`  | PATCH  | Update a task’s status or deadline               |

## Example (user template):
1. Signup:
- url: http://127.0.0.1:5001/users/signup
- payload:
```python
{
    "username" : "gaditya",
    "password" : "test@123",
    "email" : "gaditya@example.com",
    "role" : "admin"
}
```
- Response:
```
{
    "message": "User added successfully"
}
```
2. Login
- url: http://127.0.0.1:5001/users/login
- payload:
```
{
    "password" : "test@123",
    "email" : "gaditya@example.com"
}
```
- Response:
```
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.-hPQzFHxw"
}
```
3. get_users
- url: http://127.0.0.1:5001/users/get_users
- Authorization: Bearer Token (Pass the generated token)

response:
```
{
    "users": [
        {
            "username": "gaditya",
            "email": "gaditya@example.com",
            "role": "admin",
            "status": "Y"
        }
    ]
}
```

