from app.database import get_connection
from typing import List, Dict, Any
from datetime import datetime

def ejecutar_crud_roles(params: Dict[str, Any], opcion: int):
    try:
        conn = get_connection()  # Establece la conexión
        cursor = conn.cursor()
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

            # Convertir fechas y usuario a cadena (string)
            for result in results:
                if result.get("fecha_creacion"):
                    result["fecha_creacion"] = result["fecha_creacion"].isoformat()  # Convertir a string
                if result.get("fecha_actualizacion"):
                    result["fecha_actualizacion"] = result["fecha_actualizacion"].isoformat()  # Convertir a string
                if result.get("usuario_creacion"):
                    result["usuario_creacion"] = str(result["usuario_creacion"])  # Convertir a string
                if result.get("usuario_actualizacion"):
                    result["usuario_actualizacion"] = str(result["usuario_actualizacion"])  # Convertir a string

            return results
    except Exception as e:
        print(f"Error al ejecutar el procedimiento CRUD: {e}")
        raise  # Lanza la excepción para manejarla más arriba
    finally:
        cursor.close()
        conn.close()
