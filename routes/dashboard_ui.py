import reflex as rx
from state import TentoState

def dashboard() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Dashboard"),
            rx.text(f"Bienvenido, {TentoState.usuario}"),

            rx.hstack(
                rx.card(rx.text("Ventas Totales"), rx.heading("$18,450")),
                rx.card(rx.text("Margen Promedio"), rx.heading("62%")),
                rx.card(rx.text("Alertas Activas"), rx.heading("3")),
                spacing="4",
            ),

            rx.divider(),

            rx.text("Aquí irán gráficos de ventas, explicaciones por clima/eventos, etc."),
        ),
        padding="4",
    )
