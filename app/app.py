import reflex as rx
from routes import home, dashboard_ui, inventory_ui, sales_ui, alerts_ui, chatbot_ui

app = rx.App(
    theme=rx.theme(),
    style={"font_family": "sans-serif"},
)

app.add_page(route="/", component=home.home)
app.add_page(route="/dashboard", component=dashboard_ui.dashboard)
app.add_page(route="/inventario", component=inventory_ui.inventory)
app.add_page(route="/ventas", component=sales_ui.sales)
app.add_page(route="/alertas", component=alerts_ui.alerts)
app.add_page(route="/chat", component=chatbot_ui.chatbot)

