import reflex as rx
import httpx

class ChatState(rx.State):
    user_id: str = ""
    pregunta: str = ""
    respuesta: str = ""
    loading: bool = False

    async def enviar_pregunta(self):
        self.loading = True
        try:
            async with httpx.AsyncClient() as client:
                res = await client.post("http://localhost:8000/chat", json={
                    "user_id": self.user_id,
                    "pregunta": self.pregunta
                })
                self.respuesta = res.json().get("respuesta", "Error al obtener respuesta")
        except Exception as e:
            self.respuesta = f"Error: {str(e)}"
        self.loading = False

def chatbot() -> rx.Component:
    return rx.vstack(
        rx.heading("Chat IA"),
        rx.input(placeholder="ID de usuario", value=ChatState.user_id, on_change=lambda e: ChatState.set_user_id(e.target.value)),
        rx.textarea(placeholder="Escribe tu pregunta...", value=ChatState.pregunta, on_change=lambda e: ChatState.set_pregunta(e.target.value)),
        rx.button("Enviar", on_click=ChatState.enviar_pregunta, is_loading=ChatState.loading),
        rx.box(
            rx.text("Respuesta:"),
            rx.code(ChatState.respuesta),
            padding="1em",
            background_color="#f9f9f9",
            border_radius="md",
            border="1px solid #ccc",
        ),
        width="600px",
        spacing="4"
    )
