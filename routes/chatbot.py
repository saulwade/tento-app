# ✅ routes/chatbot.py

from fastapi import APIRouter
from api.openai_utils import ask_gpt
from api.supabase_client import supabase
from datetime import datetime

router = APIRouter()

@router.post("/chat")
def chat_restaurante(user_id: str, pregunta: str):
    # Obtener contexto del usuario (ventas, inventario, alertas)
    inventario = supabase.table("inventory").select("producto", "cantidad", "precio_unitario").eq("user_id", user_id).execute().data
    ventas = supabase.table("sales").select("fecha", "total", "canal").eq("user_id", user_id).execute().data
    alertas = supabase.table("alerts").select("tipo", "mensaje", "fecha").eq("user_id", user_id).execute().data

    # Preparar prompt
    contexto = f"INVENTARIO: {inventario}\nVENTAS: {ventas}\nALERTAS: {alertas}"
    prompt = f"Con base en esta info: {contexto} Responde la siguiente pregunta del dueño del restaurante: '{pregunta}'"

    # Consultar a GPT
    respuesta = ask_gpt(prompt)

    # Guardar en logs
    supabase.table("chat_logs").insert({
        "user_id": user_id,
        "pregunta": pregunta,
        "respuesta": respuesta,
        "fecha": str(datetime.now())
    }).execute()

    return {"respuesta": respuesta}
