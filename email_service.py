import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import REMITENTE, CONTRASENA, SMTP_SERVIDOR, SMTP_PUERTO

class EmailService:

    @staticmethod
    def enviar(destinatario, asunto, mensaje_texto):
        mensaje = MIMEMultipart()
        mensaje["From"] = REMITENTE
        mensaje["To"] = destinatario
        mensaje["Subject"] = asunto

        mensaje.attach(MIMEText(mensaje_texto, "plain"))

        servidor = smtplib.SMTP(SMTP_SERVIDOR, SMTP_PUERTO)
        servidor.starttls()
        servidor.login(REMITENTE, CONTRASENA)
        servidor.sendmail(REMITENTE, destinatario, mensaje.as_string())
        servidor.quit()
