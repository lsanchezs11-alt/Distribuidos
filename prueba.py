import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_correo(destinatario, asunto, mensaje_texto):
    # Configuración
    remitente = "dmartinezc10@ucentral.edu.co"
    contraseña = "soob mcdd lexc nxcu"
    
    # Crear mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto
    
    # Agregar cuerpo del mensaje
    mensaje.attach(MIMEText(mensaje_texto, 'plain'))
    
    try:
        # Conectar al servidor SMTP de Gmail (la mayoría de instituciones usan Gmail)
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(remitente, contraseña)
        
        # Enviar correo
        texto = mensaje.as_string()
        servidor.sendmail(remitente, destinatario, texto)
        servidor.quit()
        
        print(f"✓ Correo enviado exitosamente a {destinatario}")
        return True
        
    except Exception as e:
        print(f"✗ Error al enviar correo: {e}")
        return False

# Ejemplo de uso
if __name__ == "__main__":
    destinatario = "lsanchezs11@ucentral.edu.co"  # Cambia esto
    asunto = "Prueba de correo"
    mensaje = "Este es un correo de prueba enviado desde Python."
    
    enviar_correo(destinatario, asunto, mensaje)