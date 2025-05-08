import os
import pyodbc
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

def get_connection():
    """Establece una conexión con la base de datos utilizando pyodbc."""
    try:
        # Obtener las credenciales del archivo .env
        driver = os.getenv("DB_DRIVER")
        server = os.getenv("DB_SERVER")
        port = os.getenv("DB_PORT")
        database = os.getenv("DB_NAME")
        username = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")

        # Validar que todas las variables estén definidas
        if not all([driver, server, port, database, username, password]):
            raise ValueError("Faltan variables en el archivo .env")

        # Construcción de la cadena de conexión
        conn_str = (
            f"DRIVER={{{driver}}};"
            f"SERVER={server},{port};"
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password};"
            f"TrustServerCertificate=yes;"  # Evita problemas con SSL en conexiones remotas
        )

        # Intentar la conexión
        conn = pyodbc.connect(conn_str, autocommit=True)
        return conn

    except pyodbc.Error as e:
        print(f"Error de conexión a la base de datos: {e}")
        return None
    except ValueError as e:
        print(f"Error en variables de entorno: {e}")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None

def test_db_connection():
    """Verifica si la conexión a la base de datos es exitosa."""
    try:
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1")
            conn.close()
            print("Conexión a la base de datos exitosa.")
            return True
        else:
            print("Fallo en la conexión a la base de datos.")
            return False
    except Exception as e:
        print(f"Error al probar la conexión: {e}")
        return False

