# state.py
import reflex as rx

class TentoState(rx.State):
    """Estado global de la app Tento."""

    # Variables generales
    usuario: str = ""
    plan: str = "pro"
    alerta: str = ""
    mensaje_chat: str = ""
    respuesta_chat: str = ""

    # Métodos
    def set_usuario(self, nombre: str):
        self.usuario = nombre

    def set_plan(self, plan_nuevo: str):
        self.plan = plan_nuevo

    def limpiar_alerta(self):
        self.alerta = ""

    def enviar_mensaje_chat(self, mensaje: str):
        self.mensaje_chat = mensaje
        # Aquí podrías llamar un endpoint que procese la IA
        self.respuesta_chat = f"Respuesta a: {mensaje}"  # Esto luego lo conectamos con OpenAI
