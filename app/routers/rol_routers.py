from fastapi import APIRouter, HTTPException
from app.models import rol_models
from app.schemas import rol_schemas
from typing import List

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.post("/crear")
def crear_rol(rol: rol_schemas.RolBase):
    rol_id = rol_models.ejecutar_crud_roles(rol.dict(), opcion=1)
    if rol_id:
        return {"mensaje": "Rol creado exitosamente", "id_rol": rol_id}
    raise HTTPException(status_code=400, detail="Error al crear el rol")

@router.put("/actualizar")
def actualizar_rol(rol: rol_schemas.RolUpdate):
    rol_id = rol_models.ejecutar_crud_roles(rol.dict(), opcion=2)
    if rol_id:
        return {"mensaje": "Rol actualizado", "id_rol": rol_id}
    raise HTTPException(status_code=400, detail="Error al actualizar el rol")

@router.delete("/eliminar")
def eliminar_rol(rol: rol_schemas.RolDelete):
    rol_id = rol_models.ejecutar_crud_roles(rol.dict(), opcion=3)
    if rol_id:
        return {"mensaje": "Rol eliminado", "id_rol": rol_id}
    raise HTTPException(status_code=400, detail="Error al eliminar el rol")

@router.get("/listar", response_model=List[rol_schemas.RolOut])
def listar_roles():
    result = rol_models.ejecutar_crud_roles({}, opcion=4)
    return result

@router.get("/empresa/{id_empresa}", response_model=List[rol_schemas.RolOut])
def listar_roles_por_empresa(id_empresa: int):
    result = rol_models.ejecutar_crud_roles({"id_empresa": id_empresa}, opcion=5)
    return result
