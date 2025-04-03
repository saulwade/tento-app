from fastapi import APIRouter
from datetime import date

router = APIRouter(prefix="/weather-insights")

@router.get("/")
async def weather_insights(user_id: str, fecha: date = date.today()):
    # Aquí iría luego la lógica real cruzando clima y ventas con Supabase + API clima
    return {
        "user_id": user_id,
        "fecha": fecha,
        "insight": "Tus ventas bajaron por lluvia y quincena 🌀💸"
    }
