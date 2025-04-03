import reflex as rx

def inventory() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Inventario"),
            rx.text("Carga, visualiza y edita tus productos"),
            rx.divider(),

            rx.data_table(
                data=[
                    {"Producto": "Queso Oaxaca", "Unidad": "kg", "Cantidad": "5", "Precio": "$120"},
                    {"Producto": "Tortillas", "Unidad": "kg", "Cantidad": "10", "Precio": "$18"},
                    {"Producto": "Carne Asada", "Unidad": "kg", "Cantidad": "7", "Precio": "$185"},
                ],
                columns=[
                    {"header": "Producto", "accessor_key": "Producto"},
                    {"header": "Unidad", "accessor_key": "Unidad"},
                    {"header": "Cantidad", "accessor_key": "Cantidad"},
                    {"header": "Precio", "accessor_key": "Precio"},
                ],
                pagination=True,
                search=True,
                sort=True,
            ),

            rx.button("Subir archivo Excel (.xlsx)", variant="outline"),
            rx.button("Limpiar con IA", variant="solid", color_scheme="blue"),
        ),
        padding="4",
    )
