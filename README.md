🔹 ¿Qué incluye este README?
✅ Instrucciones claras de instalación
✅ Configuración del entorno y variables
✅ Comando correcto para desplegar la API
✅ Uso de entorno virtual

Crear y Activar Entorno Virtual
Para mantener tu entorno limpio y evitar conflictos de dependencias, se recomienda usar un entorno virtual. Sigue estos pasos:

Crear el entorno virtual (solo la primera vez):
python -m venv venv

Activar el entorno virtual:

En Windows:
venv\Scripts\activate

En macOS / Linux:
source venv/bin/activate

Desactivar el entorno virtual cuando termines de trabajar:
deactivate

Instalar Dependencias
Ejecuta el siguiente comando para instalar todas las dependencias necesarias:
pip install -r requirements.txt

Configurar Variables de Entorno
Agrega un archivo .env con el siguiente contenido, completando los campos según tu configuración:

DB_DRIVER=ODBC Driver 17 for SQL Server
DB_SERVER=apptualizate.cj6px0tl7fg1.us-east-2.rds.amazonaws.com
DB_PORT=1433
DB_NAME=RECONOCIMIENTO_FACIAL
DB_USER=""
DB_PASSWORD=""

Ejecutar la API
Para iniciar la API, usa el siguiente comando:
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload