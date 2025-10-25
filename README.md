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
✅ **Integrated with SOA service (SOA_AGENT) for sending welcome letter to user post registration.**   
✅ **NGINX as Load Balancer for easy scaling.**
✅ **APScheduler.** for scheduling alert to the member for Opened or Inprogress tasks.



### Tech Stack  
- **Backend:** Flask
- **Database:** MongoDB, Memcached
- **Authentication:** JWT
- **Containerization:** Docker
- **Load Balancer**: NGINX
- **APScheduler**: For scheduling tasks

### Setup Application
1. Clone the Repo
2. Update the `.env` file with required details
3. Run the command: `docker-compose up --build`
4. From next time run the command: `docker compose up` or `docker compose up -d` in detach mode.
5. nginx will be running on port:80, access your app there.

<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/1bb5f4d4-5f87-4261-adaa-36324333de5f" />


### Rabbitmq
<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/0a83a0b4-5cb8-431f-83ae-31e738f6816e" />

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

### Example (Use nginx port for below request for processing at multiple web server):

### User Template
**Signup:**

<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/248e535f-88dc-4509-9b74-a344b1f76851" />

<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/c680781c-1b29-495f-9d29-cf64e0b993aa" />

**Login**

<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/9784e32d-8585-4ca9-b5f9-87d1c76dbe0d" />

**get_users**

<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/54d7e378-c8c1-42c8-b5dd-5fb1181c6500" />

**Change Password**

<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/52fcb2e3-bc5e-4bb1-85f3-d0244541956a" />

### Task Template

**Create Task**

<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/9cf4b9b6-2aa9-46c0-aeef-9370521e0b25" />
   
**Get Tasks**

<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/3ca69134-afeb-448f-b28e-bfca802f1c80" />
   
**Get User Assigned Task**

<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/70c18011-f2c4-4b3c-844e-015c5b3fd226" />


### Scheduler Template

**Schedule Tasks**

<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/636d0c52-9643-45a3-b3ac-708fc077432f" />

**Get scheduled Tasks**

<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/2b0d7f9a-045b-497a-807c-c14e971da18b" />


