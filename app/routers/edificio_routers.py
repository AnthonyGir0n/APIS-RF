from fastapi import APIRouter, HTTPException
from app.schemas.edificio_schemas import EdificioCreate, EdificioUpdate, EdificioDelete
from app.models import edificio_models

router = APIRouter(
    prefix="/edificio",
    tags=["Edificio"]
)

@router.post("/crear")
def crear_edificio(data: EdificioCreate):
    try:
        return edificio_models.crear_edificio(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/actualizar")
def actualizar_edificio(data: EdificioUpdate):
    try:
        return edificio_models.actualizar_edificio(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/eliminar")
def eliminar_edificio(data: EdificioDelete):
    try:
        return edificio_models.eliminar_edificio(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/listar")
def listar_edificio():
    try:
        return edificio_models.obtener_edificio()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/listar_empresa/{id_empresa}")
def listar_edificio_por_empresa(id_empresa: int):
    try:
        return edificio_models.obtener_edificio_por_empresa(id_empresa)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))