## 💬 AI Chat App
----------------------------------------------------------------------------------------------------
## Project Overview
-------------------------------------------------------------------------------------------------------
A full-stack AI Chat Application built with FastAPI (backend), PostgreSQL (database), and a React frontend.
The app allows users to chat with an AI assistant, with user sessions and chat history stored in the database.


## Features
-----------------------------------------------------------------------------------------------------------------
🔐 User authentication with PostgreSQL.
💾 Persistent chat sessions stored in database.
🤖 AI chatbot powered by FastAPI backend.
⚡ Real-time message exchange via REST API.
📊 PostgreSQL schema for users, sessions, and messages.

## Technology Stack
---------------------------------------------------------------------------------------------------------------------------------------
### Backend
FastAPI – Python web framework
Uvicorn – ASGI server
PostgreSQL – Database
SQLAlchemy – ORM

### Frontend
React – UI framework
Fetch API – API requests


### ⚙️ Setup Instructions
----------------------------------------------------------------------------------------------------------------------------------
### 1) Clone Repo
git clone https://github.com/rahimathulla08/chat-app.git
cd chat-app


### 2) Setup Backend
cd backend
pip install -r requirements.txt

Run FastAPI server:
uvicorn app.main:app --reload
Backend will be available at:
👉 http://127.0.0.1:8000


### 3) Setup Database
Run PostgreSQL via Docker:

docker run -e POSTGRES_USER=app \
           -e POSTGRES_PASSWORD=password \
           -e POSTGRES_DB=aichat \
           -p 5432:5432 \
           -d --name pg postgres:15


### 4) Setup Frontend
cd src
npm install
npm start
Frontend will run at:
👉 http://localhost:3000


## 📡 API Example
----------------------------------------------------------------------------------------------------------------------------
Send Message
POST /chat

Request body:
{
  "session_id": "12345",
  "message": "Hello AI!"
}

Response:
{
  "reply": "Hi there! How can I help you today?"
}

## 🐳 Docker (Optional)
--------------------------------------------------------------------------------------------------------------------
Run everything (backend + database) with Docker Compose:

docker-compose up --build

## Screenshots:
====
(Include screenshots of the application, multi-provider switching, database tables, and error handling examples.)
![alt text](Screenshot(1).-1.jpg)
![alt text](Screenshot(2)..-1.jpg)

## Team Members
--------------------------------------------------------------------------------------------------------------------
G Naga Lasya(2451-22-748-062) - Frontend Development & UI/UX
-Mohammad Rahimathulla(2451-22-748-303) - Backend Development & Database Design-

## ---------------------------------------------------------------------------------------------------------------------

## Thank You
