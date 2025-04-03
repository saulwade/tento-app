# ✅ routes/inventory.py (Backend)
from fastapi import APIRouter, UploadFile, File
from api.supabase_client import supabase
import pandas as pd

router = APIRouter()

@router.post("/upload-inventory")
async def upload_inventory(file: UploadFile = File(...)):
    df = pd.read_excel(file.file)

    required = {"producto", "unidad", "cantidad", "precio"}
    if not required.issubset(df.columns):
        return {"error": "Formato inválido"}

    for _, row in df.iterrows():
        supabase.table("inventory").insert({
            "user_id": "demo-id",
            "producto": row["producto"],
            "unidad": row["unidad"],
            "cantidad": row["cantidad"],
            "precio_unitario": row["precio"]
        }).execute()

    return {"status": "Inventario guardado con éxito"}