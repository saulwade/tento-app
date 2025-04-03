from fastapi import APIRouter

router = APIRouter(prefix="/chat")

@router.post("/")
async def chat_with_restaurant():
    return {"response": "Hola, soy tu restaurante inteligente."}
