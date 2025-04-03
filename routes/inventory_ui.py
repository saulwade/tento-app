import reflex as rx

def inventory() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Inventario"),
            rx.text("Carga, visualiza y edita tus productos"),
            rx.divider(),

            rx.table(
                headers=["Producto", "Unidad", "Cantidad", "Precio"],
                rows=[
                    ["Queso Oaxaca", "kg", "5", "$120"],
                    ["Tortillas", "kg", "10", "$18"],
                    ["Carne Asada", "kg", "7", "$185"]
                ],
                border=True,
            ),

            rx.button("Subir archivo Excel (.xlsx)", variant="outline"),
            rx.button("Limpiar con IA", variant="solid", color_scheme="blue"),
        ),
        padding="4",
    )
