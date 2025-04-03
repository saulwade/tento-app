# ✅ routes/dashboard.py (Backend)
from fastapi import APIRouter
from api.supabase_client import supabase

router = APIRouter()

@router.get("/dashboard")
def dashboard_summary():
    # Consulta total de ventas
    ventas = supabase.table("sales").select("total").execute()
    total_ventas = sum(item["total"] for item in ventas.data)

    # Consulta alertas activas
    alertas = supabase.table("alerts").select("*").execute()
    total_alertas = len(alertas.data)

    # Margen estimado fijo de ejemplo
    margen_promedio = "62%"

    return {
        "total_ventas": total_ventas,
        "alertas_activas": total_alertas,
        "margen_promedio": margen_promedio
    }
