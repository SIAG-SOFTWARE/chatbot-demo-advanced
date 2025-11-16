# 🤖 SIAG Software – Advanced AI Chatbot Demo  
**FastAPI + React + ChatGPT API + Session Memory**

This repository showcases a **professional-grade chatbot architecture**, designed as a demonstration of how SIAG Software builds real, scalable AI products for clients.

It includes:

- Full-stack implementation (FastAPI backend + React/Vite frontend)  
- Real ChatGPT API integration  
- Session-based memory (context persists per user)  
- Clean, modern UI  
- Modular, production-oriented code structure  
- Environment-based configuration (secure API key handling)

---

## 🚀 Features

### ✅ **Real AI Integration**
The backend communicates directly with the **OpenAI ChatGPT API**.  
Clients can plug in *their own API keys* without modifying the code.

### ✅ **Session Memory**
Each user gets a unique session ID that preserves conversation context.

### ✅ **Modern Tech Stack**
- **Backend:** FastAPI, Uvicorn, httpx  
- **Frontend:** React + Vite  
- **CORS enabled**  
- Clean folder organization

### ✅ **Easy to Deploy**
- Works locally out of the box  
- Ready for Render / Railway / Docker / VPS / Nginx  
- No vendor lock-in

---
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
---

## ⚙️ Backend Setup (FastAPI)

### 1. Install dependencies

```bash
cd backend
pip install -r requirements.txt
2. Create .env file
ini
Copiar código
OPENAI_API_KEY=your_api_key_here
3. Run the server
bash
Copiar código
uvicorn main:app --reload --port 8000
Backend will be available at:

arduino
Copiar código
http://localhost:8000
🎨 Frontend Setup (React + Vite)
1. Install dependencies
bash
Copiar código
cd frontend
npm install
2. Start development server
bash
Copiar código
npm run dev
Frontend will run on:

arduino
Copiar código
http://localhost:5173
🔌 Connecting Frontend ↔ Backend
By default, the frontend expects the backend on:

bash
Copiar código
http://localhost:8000/chat
Both tools automatically work together in dev mode.

🧠 About Session Memory
Each chat session stores the last 5 messages:

User messages

AI replies

This provides contextual continuity without using a database.

Memory resets when the backend restarts (demo-friendly).

🛡 Environment & Security
No API keys stored in frontend

.env file excluded via .gitignore

OpenAI key stays server-side

Safe for client demos

🏢 About SIAG Software
SIAG Software builds pragmatic and scalable software solutions including:

AI Business Chatbots

Workflow Automation (n8n / Make / API integrations)

Custom Web Scrapers

Full-Stack Web Applications

🌐 Website: coming soon
📩 Contact: siag.software@protonmail.com

📜 License
MIT License — Free to use for learning and demos.
For commercial implementation and consulting, contact SIAG Software.

✨ Author
Developed by SIAG Software
“Automation + Intelligence = SIAG Software”
