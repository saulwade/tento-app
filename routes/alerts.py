from fastapi import APIRouter

router = APIRouter(prefix="/generate-alerts")

@router.post("/")
async def generate_alerts():
    return {"message": "Alertas generadas"}
