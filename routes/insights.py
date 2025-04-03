# ✅ routes/insights.py (Backend)
from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/weather-insights")
def weather_insights():
    return {
        "fecha": datetime.now().date().isoformat(),
        "mensaje": "Tus ventas bajaron 18% el martes. Posible causa: lluvia + fin de quincena."
    }
