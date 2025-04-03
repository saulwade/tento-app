from fastapi import APIRouter

router = APIRouter(prefix="/upload-inventory")

@router.post("/")
async def upload_inventory():
    return {"status": "ok"}
