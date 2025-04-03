import reflex as rx
import httpx

class ChatState(rx.State):
    user_id: str = ""
    pregunta: str = ""
    respuesta: str = ""
    loading: bool = False

    async def enviar_pregunta(self):
        self.set(loading=True)
        try:
            async with httpx.AsyncClient() as client:
                res = await client.post("http://localhost:8000/chat", json={
                    "user_id": self.user_id,
                    "pregunta": self.pregunta
                })
                data = res.json()
                self.set(respuesta=data.get("respuesta", "Error al obtener respuesta"))
        except Exception as e:
            self.set(respuesta=f"Error: {str(e)}")
        self.set(loading=False)

def chatbot() -> rx.Component:
    return rx.vstack(
        rx.heading("Chat con tu restaurante", size="6"),
        rx.input(
            placeholder="ID de usuario",
            value=ChatState.user_id,
            on_change=ChatState.set_user_id,
            width="100%"
        ),
        rx.text_area(
            placeholder="Escribe tu pregunta...",
            value=ChatState.pregunta,
            on_change=ChatState.set_pregunta,
            width="100%",
            height="100px"
        ),
        rx.button("Enviar", on_click=ChatState.enviar_pregunta, is_loading=ChatState.loading),
        rx.box(
            rx.text("Respuesta:"),
            rx.code(ChatState.respuesta, width="100%"),
            padding="1em",
            background_color="#f7f7f7",
            border_radius="md",
            border="1px solid #ccc",
            width="100%"
        ),
        spacing="4",
        align_items="start",
        width="600px"
    )
