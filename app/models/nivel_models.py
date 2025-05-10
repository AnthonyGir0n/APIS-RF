import pyodbc
from app.schemas.nivel_schemas import NivelCreate, NivelUpdate, NivelDelete

# Configuración de conexión
def get_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=RECONOCIMIENTO_FACIAL;'
        'Trusted_Connection=yes;'
    )

def crear_nivel(data: NivelCreate):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        EXEC CRUDNIVEL @ID_EDIFICIO = ?, @NOMBRE = ?, @USUARIO_CREACION = ?, @opcion=1
    """, data.id_edificio, data.nombre, data.usuario_creacion)
    result = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return {"id_nivel": result[0]}

def actualizar_nivel(data: NivelUpdate):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        EXEC CRUDNIVEL @ID_EDIFICIO = ?, @NOMBRE = ?, @USUARIO_ACTUALIZACION = ?, @opcion=2
    """, data.id_edificio, data.nombre, data.usuario_actualizacion)
    result = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return {"id_nivel": result[0]}

def eliminar_nivel(data: NivelDelete):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        EXEC CRUDNIVEL @ID_NIVEL=?, @USUARIO_ACTUALIZACION=?, @opcion=3
    """, data.id_nivel, data.usuario_actualizacion)
    result = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return {"id_nivel": result[0]}

def obtener_nivel():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC CRUDNIVEL @opcion=4")
    columnas = [col[0] for col in cursor.description]
    resultados = [dict(zip(columnas, row)) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return resultados

def obtener_nivel_por_edificio(id_edificio: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC CRUDNIVEL @ID_EDIFICIO=?, @opcion=5", id_edificio)
    columnas = [col[0] for col in cursor.description]
    resultados = [dict(zip(columnas, row)) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return resultados