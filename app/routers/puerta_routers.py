from fastapi import APIRouter, HTTPException
from app.models import puerta_models
from app.schemas import puerta_schemas
from typing import List

router = APIRouter(prefix="/puertas", tags=["Puertas"])

@router.post("/crear")
def crear_puerta(data: puerta_schemas.PuertaCreate):
    puerta_id = puerta_models.ejecutar_crud_puertas(data.dict(), opcion=1)
    if puerta_id:
        return {"mensaje": "Puerta creada exitosamente", "id_puerta": puerta_id}
    raise HTTPException(status_code=400, detail="Error al crear la puerta")

@router.put("/actualizar")
def actualizar_puerta(data: puerta_schemas.PuertaUpdate):
    puerta_id = puerta_models.ejecutar_crud_puertas(data.dict(), opcion=2)
    if puerta_id:
        return {"mensaje": "Puerta actualizada", "id_puerta": puerta_id}
    raise HTTPException(status_code=400, detail="Error al actualizar la puerta")

@router.delete("/eliminar")
def eliminar_puerta(data: puerta_schemas.PuertaDelete):
    puerta_id = puerta_models.ejecutar_crud_puertas(data.dict(), opcion=3)
    if puerta_id:
        return {"mensaje": "Puerta eliminada", "id_puerta": puerta_id}
    raise HTTPException(status_code=400, detail="Error al eliminar la puerta")

@router.get("/listar", response_model=List[puerta_schemas.PuertaOut])
def listar_puertas():
    result = puerta_models.ejecutar_crud_puertas({}, opcion=4)
    return result

@router.get("/nivel/{id_nivel}", response_model=List[puerta_schemas.PuertaOut])
def listar_puertas_por_nivel(id_nivel: int):
    result = puerta_models.ejecutar_crud_puertas({"id_nivel": id_nivel}, opcion=5)
    return result
