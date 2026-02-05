import tkinter as tk
from tkinter import scrolledtext
from controller import CorreoController

class AplicacionCorreo:

    def __init__(self, ventana):
        self.controller = CorreoController()
        self.ventana = ventana
        self.ventana.title("Enviar Correo")
        self.ventana.geometry("600x500")
        self.ventana.resizable(False, False)

        tk.Label(ventana, text="Para:").pack()
        self.destinatario = tk.Entry(ventana, width=50)
        self.destinatario.pack()

        tk.Label(ventana, text="Asunto:").pack()
        self.asunto = tk.Entry(ventana, width=50)
        self.asunto.pack()

        tk.Label(ventana, text="Mensaje:").pack()
        self.mensaje = scrolledtext.ScrolledText(ventana, width=50, height=15)
        self.mensaje.pack()

        tk.Button(
            ventana,
            text="Enviar",
            command=self.enviar
        ).pack(pady=10)

    def enviar(self):
        self.controller.enviar_correo(
            self.destinatario.get(),
            self.asunto.get(),
            self.mensaje.get("1.0", tk.END).strip()
        )
