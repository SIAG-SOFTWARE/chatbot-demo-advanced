from fastapi import APIRouter, Request, Response
from services.ai_engine import generate_reply
from services.session_manager import session_manager
from models import ChatMessage, ChatResponse
import uuid

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(msg: ChatMessage, request: Request, response: Response):
    session_id = request.cookies.get("session_id")

    if not session_id:
        session_id = str(uuid.uuid4())
        response.set_cookie(key="session_id", value=session_id)

    history = session_manager.get_session(session_id)
    bot_response = await generate_reply(history, msg.message)

    session_manager.update_session(session_id, msg.message, bot_response)

    return ChatResponse(reply=bot_response)

