from fastapi import APIRouter
from pydantic import BaseModel
from api.openai_utils import ask_chat

router = APIRouter()

class ChatRequest(BaseModel):
    user_id: str
    pregunta: str

@router.post("/chat")
async def chat(request: ChatRequest):
    respuesta = await ask_chat(request.user_id, request.pregunta)
    return {"respuesta": respuesta}
