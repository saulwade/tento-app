# ✅ Este archivo contiene funciones clave para 4.1
# Guarda este archivo como utils/functions.py (o en otro archivo si ya lo tienes)

from datetime import datetime, timedelta
from typing import List, Dict
from api.supabase_client import supabase
import statistics

# -----------------------------
# 1. Calcular margen y food cost
# -----------------------------
def calcular_margen(precio_venta: float, costo: float) -> float:
    if precio_venta == 0:
        return 0
    margen = ((precio_venta - costo) / precio_venta) * 100
    return round(margen, 2)

# -----------------------------
# 2. Detección de merma
# -----------------------------
def detectar_merma(user_id: str) -> List[Dict]:
    inventario_actual = supabase.table("inventory").select("*").eq("user_id", user_id).execute().data
    ventas = supabase.table("sales").select("*").eq("user_id", user_id).execute().data

    productos_vendidos = set()
    for venta in ventas:
        for item in venta.get("items", []):
            productos_vendidos.add(item["producto"])

    alertas = []
    for item in inventario_actual:
        if item["cantidad"] < item.get("cantidad_anterior", item["cantidad"]):
            if item["producto"] not in productos_vendidos:
                alertas.append({
                    "producto": item["producto"],
                    "mensaje": "Posible merma detectada"
                })
    return alertas

# -----------------------------
# 3. Detección de cambio de precio o margen
# -----------------------------
def detectar_anomalias_precios(user_id: str) -> List[Dict]:
    inventario = supabase.table("inventory").select("*").eq("user_id", user_id).execute().data
    alertas = []

    for item in inventario:
        historico = item.get("historial_precios", [])  # simulado como lista de floats
        if not historico:
            continue
        promedio = statistics.mean(historico)
        actual = item["precio_unitario"]

        if actual > promedio * 1.2:
            alertas.append({
                "producto": item["producto"],
                "mensaje": "Precio alto respecto al histórico"
            })
    return alertas

# -----------------------------
# 4. Verificar stock mínimo
# -----------------------------
def verificar_stock_minimo(user_id: str) -> List[Dict]:
    inventario = supabase.table("inventory").select("*").eq("user_id", user_id).execute().data
    alertas = []

    for item in inventario:
        minimo = item.get("stock_minimo", 0)
        if item["cantidad"] < minimo:
            alertas.append({
                "producto": item["producto"],
                "mensaje": "Stock bajo o crítico"
            })
    return alertas

# -----------------------------
# 5. Cruzado de ventas con clima/eventos (simplificado)
# -----------------------------
def analizar_clima_evento(user_id: str, fecha: str, clima: str, es_feriado: bool) -> Dict:
    ventas = supabase.table("sales").select("*").eq("user_id", user_id).eq("fecha", fecha).execute().data
    if not ventas:
        return {}

    total = sum([v["total"] for v in ventas])
    mensaje = ""
    if total < 500:  # este umbral puedes ajustarlo
        causas = []
        if clima in ["Rain", "Thunderstorm"]:
            causas.append("lluvia")
        if es_feriado:
            causas.append("feriado")

        if causas:
            mensaje = f"Ventas bajas ({total}) posiblemente por: {', '.join(causas)}."
            return {"fecha": fecha, "mensaje": mensaje}

    return {}

# -----------------------------
# 6. Agrupar ventas por canal
# -----------------------------
def ventas_por_canal(user_id: str) -> Dict[str, float]:
    ventas = supabase.table("sales").select("*").eq("user_id", user_id).execute().data
    resumen = {}
    for venta in ventas:
        canal = venta.get("canal", "Otro")
        resumen[canal] = resumen.get(canal, 0) + venta["total"]
    return resumen
