🤖 SIAG Software — Advanced Chatbot Demo

FastAPI + React + ChatGPT API + Session Memory

A production-ready example showcasing how SIAG Software builds modern AI chatbots with clean architecture, modular services, and real LLM integration.

This demo shows:
✔ FastAPI backend with ChatGPT API
✔ React frontend with live chat
✔ Session-based short-term memory
✔ Clear folder structure for scaling into enterprise apps

🚀 Features
Backend (FastAPI)

Clean router separation (/chat)

AI engine service using OpenAI ChatGPT API

Simple session memory stored server-side

Environment-based configuration (.env)

Frontend (React + Vite)

Clean minimal UI

Real-time chat messages

API helper for clean requests

Fully portable to any website or mobile app

🔧 Backend – Installation & Run
1. Install dependencies
cd backend
pip install -r requirements.txt

2. Configure environment

Create .env from .env.example:

OPENAI_API_KEY=your_api_key_here
MODEL=gpt-4o-mini
MEMORY_TTL=300

3. Run the API
uvicorn main:app --reload --port 8000


Backend runs at:
👉 http://localhost:8000

💻 Frontend – Installation & Run
1. Install dependencies
cd frontend
npm install

2. Start Vite dev server
npm run dev


Frontend runs at:
👉 http://localhost:5173

🔗 How It Works
Message Flow

User sends message (React)

Frontend → FastAPI (POST /chat)

Backend:

Stores message in session memory

Sends conversation context to ChatGPT

Returns AI answer

Frontend displays response

Memory Engine

Session memory is lightweight and designed for demos:

Stores last N messages

Auto-expires with TTL

Can be upgraded to Redis / DB easily

🧪 Example Request (Backend)
POST /chat
{
  "session_id": "abc123",
  "message": "Hello chatbot!"
}

🔐 Environment Variables
Variable	Description
OPENAI_API_KEY	ChatGPT API key
MODEL	GPT model to use
MEMORY_TTL	Memory expiration time
📦 Production Deployment

This project supports deployment to:

Docker

Railway

Render

AWS Lambda

Netlify (frontend)

If you want, I can prepare:
✔ Dockerfile
✔ docker-compose
✔ Production env templates
✔ Deploy scripts

📄 License

MIT License — free for commercial & personal use.

👨‍💻 Created by SIAG Software

AI Automation • Chatbots • Full-stack Development
https://github.com/SIAG-SOFTWARE
