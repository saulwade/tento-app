from fastapi import APIRouter

router = APIRouter(prefix="/get-sales")

@router.get("/")
async def get_sales():
    return {"sales": []}
