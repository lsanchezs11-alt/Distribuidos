from tkinter import messagebox
from email_service import EmailService

class CorreoController:

    def enviar_correo(self, destinatario, asunto, mensaje):
        if not destinatario:
            messagebox.showerror("Error", "Debe ingresar el destinatario")
            return False

        if not asunto:
            messagebox.showerror("Error", "Debe ingresar el asunto")
            return False

        if not mensaje:
            messagebox.showerror("Error", "Debe escribir el mensaje")
            return False

        try:
            EmailService.enviar(destinatario, asunto, mensaje)
            messagebox.showinfo("Éxito", "Correo enviado correctamente")
            return True
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return False
