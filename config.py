import tkinter as tk
from tkinter import messagebox, scrolledtext
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class AplicacionCorreo:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Enviar Correo Electrónico")
        self.ventana.geometry("600x500")
        self.ventana.resizable(False, False)
        
        # Configuración del remitente
        self.remitente = "cuentadigital1225@gmail.com"
        self.contraseña = "hpke hsxb fnvt fbat"
        
        # Título
        titulo = tk.Label(ventana, text="📧 Enviar Correo Electrónico", 
                         font=("Arial", 16, "bold"), fg="#2c3e50")
        titulo.pack(pady=15)
        
        # Frame principal
        frame = tk.Frame(ventana, padx=20, pady=10)
        frame.pack(fill="both", expand=True)
        
        # Destinatario
        tk.Label(frame, text="Para:", font=("Arial", 10, "bold")).grid(
            row=0, column=0, sticky="w", pady=5)
        self.entrada_destinatario = tk.Entry(frame, width=50, font=("Arial", 10))
        self.entrada_destinatario.grid(row=0, column=1, pady=5, padx=5)
        
        # Asunto
        tk.Label(frame, text="Asunto:", font=("Arial", 10, "bold")).grid(
            row=1, column=0, sticky="w", pady=5)
        self.entrada_asunto = tk.Entry(frame, width=50, font=("Arial", 10))
        self.entrada_asunto.grid(row=1, column=1, pady=5, padx=5)
        
        # Cuerpo del mensaje
        tk.Label(frame, text="Mensaje:", font=("Arial", 10, "bold")).grid(
            row=2, column=0, sticky="nw", pady=5)
        self.texto_mensaje = scrolledtext.ScrolledText(
            frame, width=50, height=15, font=("Arial", 10), wrap=tk.WORD)
        self.texto_mensaje.grid(row=2, column=1, pady=5, padx=5)
        
        # Botón enviar
        self.boton_enviar = tk.Button(
            ventana, text="📨 Enviar Correo", font=("Arial", 12, "bold"),
            bg="#27ae60", fg="white", padx=20, pady=10,
            command=self.enviar_correo, cursor="hand2")
        self.boton_enviar.pack(pady=10)
        
        # Etiqueta de estado
        self.etiqueta_estado = tk.Label(
            ventana, text="", font=("Arial", 9), fg="#7f8c8d")
        self.etiqueta_estado.pack()
    
    def enviar_correo(self):
        # Obtener datos
        destinatario = self.entrada_destinatario.get().strip()
        asunto = self.entrada_asunto.get().strip()
        mensaje_texto = self.texto_mensaje.get("1.0", tk.END).strip()
        
        # Validar campos
        if not destinatario:
            messagebox.showerror("Error", "Por favor ingresa el destinatario")
            return
        
        if not asunto:
            messagebox.showerror("Error", "Por favor ingresa el asunto")
            return
        
        if not mensaje_texto:
            messagebox.showerror("Error", "Por favor escribe un mensaje")
            return
        
        # Deshabilitar botón mientras se envía
        self.boton_enviar.config(state="disabled", text="Enviando...")
        self.etiqueta_estado.config(text="Enviando correo...", fg="#f39c12")
        self.ventana.update()
        
        try:
            # Crear mensaje
            mensaje = MIMEMultipart()
            mensaje['From'] = self.remitente
            mensaje['To'] = destinatario
            mensaje['Subject'] = asunto
            
            # Agregar cuerpo
            mensaje.attach(MIMEText(mensaje_texto, 'plain'))
            
            # Conectar y enviar
            servidor = smtplib.SMTP('smtp.gmail.com', 587)
            servidor.starttls()
            servidor.login(self.remitente, self.contraseña)
            
            texto = mensaje.as_string()
            servidor.sendmail(self.remitente, destinatario, texto)
            servidor.quit()
            
            # Éxito
            self.etiqueta_estado.config(
                text=f"✓ Correo enviado exitosamente a {destinatario}", 
                fg="#27ae60")
            
            messagebox.showinfo(
                "Éxito", 
                f"¡Correo enviado con éxito!\n\nPara: {destinatario}\nAsunto: {asunto}")
            
            # Limpiar campos
            self.limpiar_campos()
            
        except Exception as e:
            self.etiqueta_estado.config(
                text=f"✗ Error al enviar correo", 
                fg="#e74c3c")
            messagebox.showerror("Error", f"No se pudo enviar el correo:\n\n{str(e)}")
        
        finally:
            # Rehabilitar botón
            self.boton_enviar.config(state="normal", text="📨 Enviar Correo")
    
    def limpiar_campos(self):
        self.entrada_destinatario.delete(0, tk.END)
        self.entrada_asunto.delete(0, tk.END)
        self.texto_mensaje.delete("1.0", tk.END)

# Crear y ejecutar aplicación
if __name__ == "__main__":
    ventana = tk.Tk()
    app = AplicacionCorreo(ventana)
    ventana.mainloop()
