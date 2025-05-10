import pyodbc
from app.schemas.edificio_schemas import EdificioCreate, EdificioUpdate, EdificioDelete

# Configuración de conexión
def get_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=RECONOCIMIENTO_FACIAL;'
        'Trusted_Connection=yes;'
    )

def crear_edificio(data: EdificioCreate):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        EXEC CRUDEDIFICIO @ID_EMPRESA = ?, @NOMBRE = ?, @USUARIO_CREACION = ?, @opcion=1
    """, data.id_empresa, data.nombre, data.usuario_creacion)
    result = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return {"id_edificio": result[0]}

def actualizar_edificio(data: EdificioUpdate):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        EXEC CRUDEDIFICIO @ID_EMPRESA = ?, @NOMBRE = ?, @USUARIO_ACTUALIZACION = ?, @opcion=2
    """, data.id_empresa, data.nombre, data.usuario_actualizacion)
    result = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return {"id_edificio": result[0]}

def eliminar_edificio(data: EdificioDelete):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        EXEC CRUDEDIFICIO @ID_EDIFICIO=?, @USUARIO_ACTUALIZACION=?, @opcion=3
    """, data.id_edificio, data.usuario_actualizacion)
    result = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return {"id_edificio": result[0]}

def obtener_edificio():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC CRUDEDIFICIO @opcion=4")
    columnas = [col[0] for col in cursor.description]
    resultados = [dict(zip(columnas, row)) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return resultados

def obtener_edificio_por_empresa(id_empresa: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC CRUDEDIFICIO @ID_EMPRESA=?, @opcion=5", id_empresa)
    columnas = [col[0] for col in cursor.description]
    resultados = [dict(zip(columnas, row)) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return resultados