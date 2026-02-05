# Aplicación de Envío de Correos Electrónicos en Python

## Descripción
Aplicación de escritorio desarrollada en Python que permite enviar correos electrónicos utilizando el protocolo SMTP de Gmail. El sistema fue diseñado aplicando principios de ingeniería de software y una arquitectura por capas.

## Requisitos Funcionales
- Permite enviar correos electrónicos.
- El cuerpo del correo contiene los nombres de los integrantes del equipo.
- El correo incluye el enlace al repositorio GitHub del proyecto.

## Arquitectura por Capas
El sistema está estructurado siguiendo un enfoque de arquitectura por capas y un modelo MVC simplificado:

- **Capa de Presentación (Vista)**  
  Implementada en `ui.py`, se encarga de la interfaz gráfica y la interacción con el usuario mediante Tkinter.

- **Capa de Controlador**  
  Implementada en `controller.py`, gestiona los eventos del usuario, las validaciones y las reglas de negocio.

- **Capa de Servicios / Infraestructura**  
  Implementada en `email_service.py`, se encarga de la comunicación con el servidor SMTP de Gmail.

- **Capa de Configuración**  
  Implementada en `config.py`, centraliza los parámetros de configuración del sistema.

- **Punto de Entrada**  
  Implementado en `main.py`, inicializa y ejecuta la aplicación.

## Tecnologías Utilizadas
- Python
- Tkinter
- SMTP (Gmail)
- GitHub

## Ejecución
```bash
python main.py
