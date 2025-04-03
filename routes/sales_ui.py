import reflex as rx

def sales() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Ventas"),
            rx.text("Consulta tu historial de ventas"),
            rx.divider(),

            rx.table(
                headers=["Fecha", "Canal", "Total"],
                rows=[
                    ["2025-03-01", "Rappi", "$480"],
                    ["2025-03-02", "Uber", "$690"],
                    ["2025-03-03", "Local", "$1,100"]
                ],
                border=True,
            ),
        ),
        padding="4",
    )
