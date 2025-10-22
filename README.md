## Project Description
The Task Tracker Backend is a scalable RESTful API built with Flask to efficiently manage users and tasks.
It provides secure authentication, task management, and real-time integration with RabbitMQ and Memcached for asynchronous messaging and caching.
The application is fully Dockerized, supports MongoDB, and implements robust logging for observability and debugging.

### Key Features  
✅ **User authentication & authorization (JWT-based)**  
✅ **CRUD operations for tasks** (Create, Read, Update, Delete)  
✅ **Task status updates & deadlines tracking**  
✅ **Database support** (MongoDB)    
✅ **Asynchronous task processing** using RabbitMQ    
✅ **Memcache for user session management**    
✅ **Dockerized for easy deployment**    
✅ **Logging for Debugging** using python logging module (file and console logging)    
✅ **Integrated with SOA service (SOA_AGENT) for sending welcome letter to user post registration**

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
Note: Please setup rabbitmq and Memcached and add details in .env or use docker way of installation.

### Welcome Email
<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/c680781c-1b29-495f-9d29-cf64e0b993aa" />


### Setup Application with Docker
1. Clone the Repo
2. Update the `.env` file with required details
3. Run the command: `docker-compose up --build`
4. From next time run the command: `docker compose up` or `docker compose up -d` in detach mode.


### Rabbitmq
<img width="700" height="300" alt="image" src="https://github.com/user-attachments/assets/35a20306-9c15-43bc-a0c1-9c6632e75a84" />

TODO: Setup a service to consume message from welcome queue and send welcome letter to user.

##  Endpoints Overview

| Endpoint                   | Method | Description                                      |
|----------------------------|--------|--------------------------------------------------|
| `users/signup              | POST   | Register a new user                              |
| `users/login`              | POST   | Authenticate and obtain a JWT token              |
| `users/get_users`          | GET    | Get all users for the authenticated user(admin)  |
| `/tasks/add_task`          | POST   | Create a new task                                |
| `/tasks/get_tasks`         | GET    | Get all tasks                                    |
| `/tasks/get_my_task`       | GET    | Get all the assigned task for loggedin user      |

## Example (user template):
**Signup:**
<img width="1108" height="509" alt="image" src="https://github.com/user-attachments/assets/248e535f-88dc-4509-9b74-a344b1f76851" />

**Login**
<img width="1122" height="512" alt="image" src="https://github.com/user-attachments/assets/9784e32d-8585-4ca9-b5f9-87d1c76dbe0d" />

**get_users**
<img width="1349" height="564" alt="image" src="https://github.com/user-attachments/assets/54d7e378-c8c1-42c8-b5dd-5fb1181c6500" />

**Change Password**
   <img width="1361" height="607" alt="image" src="https://github.com/user-attachments/assets/52fcb2e3-bc5e-4bb1-85f3-d0244541956a" />

**Create Task**
   <img width="1005" height="541" alt="image" src="https://github.com/user-attachments/assets/9cf4b9b6-2aa9-46c0-aeef-9370521e0b25" />
   
**Get Tasks**
   <img width="1036" height="561" alt="image" src="https://github.com/user-attachments/assets/3ca69134-afeb-448f-b28e-bfca802f1c80" />
   
**Get User Assigned Task**
   <img width="1027" height="578" alt="image" src="https://github.com/user-attachments/assets/70c18011-f2c4-4b3c-844e-015c5b3fd226" />


