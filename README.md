## Project Description
The **Task Tracker Backend** is a RESTful API built using **Flask** to manage tasks efficiently. It provides user authentication, task creation, updates, and tracking functionalities. Designed for scalability, supports integration with **SQL/NoSQL databases**.

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
3. Run the flask App
```
flask run --host=0.0.0.0 --port=5001 --reload
```
4. Stop the server (CLTRL + C)
5. Deactivate the virtual environment
```
deactivate
```