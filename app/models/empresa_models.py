import pyodbc
from app.schemas.empresa_schemas import EmpresaCreate, EmpresaUpdate, EmpresaDelete

def get_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=RECONOCIMIENTO_FACIAL;'
        'Trusted_Connection=yes;'
    )

def crear_empresa(data: EmpresaCreate):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        EXEC dbo.CRUDEMPRESA @NOMBRE = ?, @USUARIO_CREACION = ?, @opcion=1
    """, data.nombre, data. data.usuario_creacion)   
    result = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return {"id_empresa": result[0]}

def actualizar_empresa(data: EmpresaUpdate):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        EXEC CRUDEMPRESA @NOMBRE = ?, @USUARIO_CREACION = ?, @opcion=2
    """, data.nombre, data.usuario_creacion)
    result = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return {"id_empresa": result[0]}

def eliminar_empresa(data: EmpresaDelete):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        EXEC CRUDEMPRESA @ID_EMPRESA = ?, @USUARIO_ACTUALIZACION = ?, @opcion=3
    """, data.id_empresa, data.usuario_actualizacion)
    result = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return {"id_empresa": result[0]}

def obtener_empresas():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC CRUDEMPRESA @opcion=4")
    columnas = [col[0] for col in cursor.description]
    resultados = [dict(zip(columnas, row)) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return resultados
