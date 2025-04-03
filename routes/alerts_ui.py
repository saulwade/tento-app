import reflex as rx

def alerts() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Alertas del Sistema"),
            rx.text("Alertas detectadas por IA y reglas de negocio"),
            rx.divider(),

            rx.table(
                headers=["Tipo", "Mensaje", "Fecha"],
                rows=[
                    ["Margen", "Platillo X bajó 15% su rentabilidad", "2025-03-29"],
                    ["Stock", "Te queda poco de Queso Oaxaca", "2025-03-30"],
                    ["Clima", "Lluvia coincidió con baja de ventas", "2025-03-31"]
                ],
                border=True,
            ),
        ),
        padding="4",
    )
