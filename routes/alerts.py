# ✅ routes/alerts.py (actualizado para usar funciones del sistema)

from fastapi import APIRouter
from utils.functions import (
    detectar_merma,
    detectar_anomalias_precios,
    verificar_stock_minimo,
    analizar_clima_evento
)
from api.supabase_client import supabase
from datetime import date

router = APIRouter()

@router.post("/generate-alerts")
def generar_alertas(user_id: str):
    alertas_generadas = []

    # 1. Merma
    mermas = detectar_merma(user_id)
    for m in mermas:
        supabase.table("alerts").insert({
            "user_id": user_id,
            "tipo": "merma",
            "mensaje": m["mensaje"],
            "gravedad": "media",
            "fecha": str(date.today())
        }).execute()
        alertas_generadas.append(m["mensaje"])

    # 2. Precio anómalo
    precios = detectar_anomalias_precios(user_id)
    for p in precios:
        supabase.table("alerts").insert({
            "user_id": user_id,
            "tipo": "precio",
            "mensaje": p["mensaje"],
            "gravedad": "media",
            "fecha": str(date.today())
        }).execute()
        alertas_generadas.append(p["mensaje"])

    # 3. Stock bajo
    bajos = verificar_stock_minimo(user_id)
    for b in bajos:
        supabase.table("alerts").insert({
            "user_id": user_id,
            "tipo": "stock",
            "mensaje": b["mensaje"],
            "gravedad": "alta",
            "fecha": str(date.today())
        }).execute()
        alertas_generadas.append(b["mensaje"])

    # 4. Venta baja por clima/evento (simplificado)
    evento = analizar_clima_evento(user_id, str(date.today()), clima="Rain", es_feriado=True)
    if evento:
        supabase.table("alerts").insert({
            "user_id": user_id,
            "tipo": "evento",
            "mensaje": evento["mensaje"],
            "gravedad": "baja",
            "fecha": evento["fecha"]
        }).execute()
        alertas_generadas.append(evento["mensaje"])

    return {"alertas": alertas_generadas}
