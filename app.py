import reflex as rx
from routes import dashboard_ui, home, inventory_ui, sales, alerts, chatbot

app = rx.App(
    theme=rx.theme(),
    style={"font_family": "sans-serif"},
    title="Tento – BI para Restaurantes",
    description="Controla tus costos, entiende tus ventas y duerme tranquilo",
    favicon="/favicon.ico",
)

# 🔹 Páginas públicas
app.add_page("Inicio", home.home, route="/")

# 🔹 Páginas privadas o funcionales del sistema
app.add_page("Dashboard", dashboard_ui.dashboard)
app.add_page("Inventario", inventory_ui.inventory)
app.add_page("Ventas", sales.sales)
app.add_page("Alertas", alerts.alerts)
app.add_page("Chat IA", chatbot.chatbot, route="/chat")

app.compile()
