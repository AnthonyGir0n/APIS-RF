from app.database import get_connection
from typing import List, Dict, Any

def ejecutar_crud_roles(params: Dict[str, Any], opcion: int):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            EXEC crudRoles @ID_ROL=?, @ID_EMPRESA=?, @NOMBRE=?, @ESTADO=?, 
                           @USUARIO_CREACION=?, @USUARIO_ACTUALIZACION=?, @opcion=?
        """, (
            params.get("id_rol"),
            params.get("id_empresa"),
            params.get("nombre"),
            params.get("estado"),
            params.get("usuario_creacion"),
            params.get("usuario_actualizacion"),
            opcion
        ))

        if opcion in [1, 2, 3]:
            result = cursor.fetchone()
            conn.commit()
            return result[0] if result else None

        elif opcion in [4, 5]:
            columns = [column[0].lower() for column in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return results

    finally:
        cursor.close()
        conn.close()
