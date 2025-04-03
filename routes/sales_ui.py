import reflex as rx

def sales() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Ventas"),
            rx.text("Visualiza tus ventas diarias y semanales"),
            rx.divider(),

            rx.data_table(
                data=[
                    {"Fecha": "2024-03-30", "Total": "$1,250", "Canal": "Web"},
                    {"Fecha": "2024-03-31", "Total": "$980", "Canal": "Rappi"},
                    {"Fecha": "2024-04-01", "Total": "$1,430", "Canal": "Uber"},
                ],
                columns=[
                    {"header": "Fecha", "accessor_key": "Fecha"},
                    {"header": "Total", "accessor_key": "Total"},
                    {"header": "Canal", "accessor_key": "Canal"},
                ],
                pagination=True,
                search=True,
                sort=True,
            ),

            rx.button("Subir archivo de ventas (.xlsx)", variant="outline"),
            rx.button("Explicar variación", variant="solid", color_scheme="blue"),
        ),
        padding="4",
    )
