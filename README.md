🧠 SIAG Software – Advanced Chatbot Demo

FastAPI + React + OpenAI API + Session Memory

This repository showcases an advanced chatbot demo combining a modern backend (FastAPI) with a clean React frontend.
It is designed as a professional example of how SIAG Software builds scalable, production-ready conversational systems for clients.

🚀 Features

FastAPI backend (lightweight, async, production-ready)

React + Vite frontend (fast dev + modern architecture)

ChatGPT API integration (replaceable with any LLM provider)

Session-based memory (conversation persists per session)

Config-driven (.env system for API keys & settings)

Full project structure showcasing real-world architecture

📁 Repository Structure
chatbot-demo-advanced/
│
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── routers/
│   │   └── chat.py
│   ├── services/
│   │   ├── ai_engine.py
│   │   └── session_manager.py
│   ├── utils/
│   │   └── config.py
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── ChatUI.jsx
│   │   ├── api.js
│   ├── public/
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
│
└── README.md

🛠️ Backend Setup (FastAPI)
1. Install dependencies
pip install -r requirements.txt

2. Create .env

Copy .env.example → .env and fill:

OPENAI_API_KEY=your_api_key_here
MODEL=gpt-4.1-mini
MAX_TOKENS=200

3. Run the server
uvicorn main:app --reload


Backend runs at:
http://localhost:8000

🎨 Frontend Setup (React + Vite)
1. Install dependencies
npm install

2. Run dev server
npm run dev


Frontend runs at:
http://localhost:5173

Make sure backend is running first.

🔌 API Endpoint (Backend → Frontend)

POST /chat

Request:

{
  "message": "Hello"
}


Response:

{
  "reply": "Hello! How can I help you today?"
}

🧬 Session Memory

Each visitor receives a unique session ID.
Memory is stored in a lightweight in-memory dictionary for demo purposes:

remembers previous messages

preserves context

resets automatically if inactive

(Production-ready version can use Redis / Supabase / DB.)

📦 Tech Stack
Backend

FastAPI

Uvicorn

Pydantic

OpenAI API

Python 3.10+

Frontend

React

Vite

Fetch API

Modern functional components

📘 License — MIT
MIT License

Copyright (c) 2025 SIAG Software

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...


(Include full MIT text in the repo.)

🌐 About SIAG Software

SIAG Software builds AI-driven tools, workflow automation, chatbots, and custom full-stack solutions for modern businesses.

Website coming soon.
Contact: siag.software@protonmail.com
