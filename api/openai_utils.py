import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

async def ask_chat(user_id: str, pregunta: str) -> str:
    prompt = f"Usuario: {pregunta}\nRespuesta:"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Eres un asistente experto en negocios de comida."},
            {"role": "user", "content": pregunta}
        ]
    )
    return response.choices[0].message["content"].strip()
