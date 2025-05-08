### 🔹 **¿Qué incluye este README?**

✅ Instrucciones claras de instalación  
✅ Configuración del entorno y variables  
✅ Comando correcto para desplegar la API 

# Instalar Dependencias

Ejecuta el siguiente comando para instalar todas las dependencias necesarias:

```bash
pip install -r requirements.txt

# Configurar Variables de Entorno

DB_DRIVER=ODBC Driver 17 for SQL Server
DB_SERVER=apptualizate.cj6px0tl7fg1.us-east-2.rds.amazonaws.com
DB_PORT=1433
DB_NAME=RECONOCIMIENTO_FACIAL
DB_USER=""
DB_PASSWORD=""

# Ejecutar la API

Para iniciar la API, usa el siguiente comando:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
"# APIS-RF" 
