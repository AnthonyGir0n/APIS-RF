import pyodbc
from app.schemas.puerta_schemas import PuertaCreate, PuertaUpdate, PuertaDelete

# Configuración de conexión
def get_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=RECONOCIMIENTO_FACIAL;'
        'Trusted_Connection=yes;'
    )

def crear_puerta(data: PuertaCreate):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        EXEC crudPuertas @ID_NIVEL=?, @NOMBRE=?, @USUARIO_CREACION=?, @opcion=1
    """, data.id_nivel, data.nombre, data.usuario_creacion)
    result = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return {"id_puerta": result[0]}

def actualizar_puerta(data: PuertaUpdate):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        EXEC crudPuertas @ID_PUERTA=?, @ID_NIVEL=?, @NOMBRE=?, @USUARIO_ACTUALIZACION=?, @opcion=2
    """, data.id_puerta, data.id_nivel, data.nombre, data.usuario_actualizacion)
    result = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return {"id_puerta": result[0]}

def eliminar_puerta(data: PuertaDelete):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        EXEC crudPuertas @ID_PUERTA=?, @USUARIO_ACTUALIZACION=?, @opcion=3
    """, data.id_puerta, data.usuario_actualizacion)
    result = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return {"id_puerta": result[0]}

def obtener_puertas():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC crudPuertas @opcion=4")
    columnas = [col[0] for col in cursor.description]
    resultados = [dict(zip(columnas, row)) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return resultados

def obtener_puertas_por_nivel(id_nivel: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC crudPuertas @ID_NIVEL=?, @opcion=5", id_nivel)
    columnas = [col[0] for col in cursor.description]
    resultados = [dict(zip(columnas, row)) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return resultados
import pyodbc
from app.schemas.puerta_schemas import PuertaCreate, PuertaUpdate, PuertaDelete

# Configuración de conexión
def get_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=RECONOCIMIENTO_FACIAL;'
        'Trusted_Connection=yes;'
    )

def crear_puerta(data: PuertaCreate):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        EXEC crudPuertas @ID_NIVEL=?, @NOMBRE=?, @USUARIO_CREACION=?, @opcion=1
    """, data.id_nivel, data.nombre, data.usuario_creacion)
    result = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return {"id_puerta": result[0]}

def actualizar_puerta(data: PuertaUpdate):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        EXEC crudPuertas @ID_PUERTA=?, @ID_NIVEL=?, @NOMBRE=?, @USUARIO_ACTUALIZACION=?, @opcion=2
    """, data.id_puerta, data.id_nivel, data.nombre, data.usuario_actualizacion)
    result = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return {"id_puerta": result[0]}

def eliminar_puerta(data: PuertaDelete):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        EXEC crudPuertas @ID_PUERTA=?, @USUARIO_ACTUALIZACION=?, @opcion=3
    """, data.id_puerta, data.usuario_actualizacion)
    result = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return {"id_puerta": result[0]}

def obtener_puertas():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC crudPuertas @opcion=4")
    columnas = [col[0] for col in cursor.description]
    resultados = [dict(zip(columnas, row)) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return resultados

def obtener_puertas_por_nivel(id_nivel: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC crudPuertas @ID_NIVEL=?, @opcion=5", id_nivel)
    columnas = [col[0] for col in cursor.description]
    resultados = [dict(zip(columnas, row)) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return resultados
