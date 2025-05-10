from fastapi import APIRouter, HTTPException
from app.schemas.nivel_schemas import NivelCreate, NivelUpdate, NivelDelete
from app.models import nivel_models

router = APIRouter(
    prefix="/nivel",
    tags=["Nivel"]
)

@router.post("/crear")
def crear_nivel(data: NivelCreate):
    try:
        return nivel_models.crear_nivel(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/actualizar")
def actualizar_nivel(data: NivelUpdate):
    try:
        return nivel_models.actualizar_nivel(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/eliminar")
def eliminar_nivel(data: NivelDelete):
    try:
        return nivel_models.eliminar_nivel(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/listar")
def listar_nivel():
    try:
        return edificio_models.obtener_nivel()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/listar/{id_edificio}")
def listar_nivel_por_edificio(id_edificio: int):
    try:
        return nivel_models.obtener_nivel_por_edificio(id_edificio)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))