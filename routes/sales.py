# ✅ routes/sales.py (Backend)
from fastapi import APIRouter
from api.supabase_client import supabase

router = APIRouter()

@router.get("/get-sales")
def get_sales():
    data = supabase.table("sales").select("*").order("fecha", desc=True).limit(10).execute()
    return data.data
