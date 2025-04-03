# ✅ routes/home.py
import reflex as rx

def home() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Bienvenido a Tento", size="5"),
            rx.text("Controla tus costos, entiende tus ventas y duerme tranquilo."),
            rx.link("Ir al Dashboard", href="/dashboard", color="blue", margin_top="1em")
        ),
        min_height="100vh",
        padding="2em"
    )
