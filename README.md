# 🤖 SIAG Software – Advanced Chatbot Demo

**FastAPI + React + OpenAI API + Session Memory**  
Professional demo showcasing how SIAG Software builds modern, production-ready conversational systems.

---

## 🚀 Features

- **FastAPI backend** – async, lightweight, scalable  
- **React + Vite frontend** – modern and fast  
- **OpenAI ChatGPT API integration**  
- **Session-based memory** (per visitor)  
- **Clean project architecture** for real-world deployments  
- **Config-based** (.env) for easy customization  

---

## 📁 Repository Structure

```
chatbot-demo-advanced/
│
├── backend/
│ ├── main.py
│ ├── models.py
│ ├── routers/
│ │ └── chat.py
│ ├── services/
│ │ ├── ai_engine.py
│ │ └── session_manager.py
│ ├── utils/
│ │ └── config.py
│ ├── requirements.txt
│ └── .env.example
│
├── frontend/
│ ├── src/
│ │ ├── App.jsx
│ │ ├── ChatUI.jsx
│ │ ├── api.js
│ ├── public/
│ ├── index.html
│ ├── package.json
│ └── vite.config.js
│
└── README.md
```

---

## 🛠️ Backend Setup (FastAPI)

**1. Install dependencies**
```bash
pip install -r backend/requirements.txt
2. Create .env file

bash
Copiar código
cp backend/.env.example backend/.env
Fill with your values:

ini
Copiar código
OPENAI_API_KEY=your_api_key_here
MODEL=gpt-4.1-mini
MAX_TOKENS=200
3. Run backend

bash
Copiar código
uvicorn backend.main:app --reload
Backend runs at:
👉 http://localhost:8000

🎨 Frontend Setup (React + Vite)
1. Install dependencies

bash
Copiar código
cd frontend
npm install
2. Start dev server

bash
Copiar código
npm run dev
Frontend runs at:
👉 http://localhost:5173
(Backend must be running first.)

🔌 API Endpoint
POST /chat

Request:

json
Copiar código
{ "message": "Hello" }
Response:

json
Copiar código
{ "reply": "Hello! How can I help you today?" }
🧬 Session Memory
Each visitor gets a unique session token.
Memory is stored in lightweight in-memory buffers:

remembers past messages

keeps short context

resets automatically after inactivity

Production-ready deployments can switch to Redis/Supabase/DB with no code changes.

📦 Tech Stack
Backend
Python 3.10+

FastAPI

Uvicorn

Pydantic

OpenAI API

Frontend
React

Vite

Fetch API

📘 License — MIT
MIT License
Copyright (c) 2025 SIAG Software

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...

(Full MIT text included in the repository.)

🌐 About SIAG Software
SIAG Software builds AI-driven tools, workflow automation, chatbots, and custom full-stack solutions for modern businesses.

Website: coming soon
Contact: siag.software@protonmail.com
