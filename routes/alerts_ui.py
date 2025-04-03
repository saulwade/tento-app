import reflex as rx

def alerts() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Alertas del Sistema"),
            rx.text("Aquí puedes ver las alertas generadas automáticamente por Tento."),
            rx.divider(),

            rx.data_table(
                data=[
                    {"Tipo": "Merma", "Mensaje": "Queso Oaxaca bajó sin ventas", "Gravedad": "Media"},
                    {"Tipo": "Precio Alto", "Mensaje": "Carne subió 25% esta semana", "Gravedad": "Alta"},
                    {"Tipo": "Bajo Margen", "Mensaje": "Torta de Jamón bajó a 18% de utilidad", "Gravedad": "Alta"},
                ],
                columns=["Tipo", "Mensaje", "Gravedad"],
                search=True,
                sort=True,
                pagination=True,
            )
        ),
        padding="4",
    )
