# routes/ranking.py
from fastapi import APIRouter
from api.supabase_client import supabase

router = APIRouter()

@router.get("/top-products")
def top_products(user_id: str):
    data = supabase.table("sales").select("*").eq("user_id", user_id).execute()
    sales = data.data

    product_totals = {}
    for sale in sales:
        for item in sale.get("items", []):  # si guardas productos por venta
            nombre = item["producto"]
            ganancia = item["margen_unitario"] * item["cantidad"]
            product_totals[nombre] = product_totals.get(nombre, 0) + ganancia

    ranked = sorted(product_totals.items(), key=lambda x: x[1], reverse=True)

    return {"ranking": ranked}
