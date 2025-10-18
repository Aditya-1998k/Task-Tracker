## Project Description
The **Task Tracker Backend** is a RESTful API built using **Flask** to manage tasks efficiently. It provides user authentication, task creation, updates, and tracking functionalities. Designed for scalability, supports integration with **SQL/NoSQL databases**.

Deployment URL : https://task-tracker-backend-yv45.onrender.com

### Key Features  
✅ **User authentication & authorization (JWT-based)**  
✅ **CRUD operations for tasks** (Create, Read, Update, Delete)  
✅ **Task status updates & deadlines tracking**  
✅ **Database support** (MongoDB)    
✅ **Asynchronous task processing** using RabbitMQ    
✅ **Dockerized for easy deployment**    
✅ **Logging for Debugging** using python logging module (file and console logging)    

### Tech Stack  
- **Backend:** Flask
- **Database:** MongoDB, Memcached
- **Authentication:** JWT
- **Containerization:** Docker  

### Steps to Start the APP (Without Docker)
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

### Setup Application with Docker
1. Clone the Repo
2. Update the `.env` file with required details
3. Run the command: `docker-compose up --build`
4. From next time run the command: `docker compose up` or `docker compose up -d` in detach mode.

##  Endpoints Overview

| Endpoint                   | Method | Description                                      |
|----------------------------|--------|--------------------------------------------------|
| `users/signup              | POST   | Register a new user                              |
| `users/login`              | POST   | Authenticate and obtain a JWT token              |
| `users/get_users`          | GET    | Get all users for the authenticated user(admin)  |
| `/tasks`                   | POST   | Create a new task                                |
| `/tasks/<task_id>`         | PUT    | Update a specific task                           |
| `/tasks/<task_id>`         | DELETE | Delete a specific task                           |
| `/tasks/<task_id>/status`  | PATCH  | Update a task’s status or deadline               |

## Example (user template):
1. **Signup:**
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
```python
{
    "message": "User added successfully"
}
```
2. **Login**
- url: http://127.0.0.1:5001/users/login
- payload:
```python
{
    "password" : "test@123",
    "email" : "gaditya@example.com"
}
```
- Response:
```python
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.-hPQzFHxw"
}
```
3. **get_users**
- url: http://127.0.0.1:5001/users/get_users
- Authorization: Bearer Token (Pass the generated token)

response:
```python
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

