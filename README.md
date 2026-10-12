# VallasArte - Versión Python (Migrada desde PHP)

Este proyecto ha sido completamente traducido y adaptado de PHP a Python utilizando Flask y SQLAlchemy.

## Estructura del Proyecto:
- `app.py`: Aplicación web principal con todas las rutas equivalentes a los scripts PHP.
- `database.py`: Gestión de conexión y modelos de base de datos.
- `templates/`: Plantillas HTML migradas.
- `static/`: Hojas de estilo y scripts de JavaScript.
- `requirements.txt`: Dependencias necesarias.

## Cómo ejecutar la aplicación:
1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Configurar la base de datos en `database.py`.
3. Iniciar el servidor:
   ```bash
   python app.py
   ```
