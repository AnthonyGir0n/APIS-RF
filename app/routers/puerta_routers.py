from fastapi import APIRouter, HTTPException
from app.schemas.puerta_schemas import PuertaCreate, PuertaUpdate, PuertaDelete
from app.models import puerta_models

router = APIRouter(
    prefix="/puertas",
    tags=["Puertas"]
)

@router.post("/crear")
def crear_puerta(data: PuertaCreate):
    try:
        return puerta_models.crear_puerta(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/actualizar")
def actualizar_puerta(data: PuertaUpdate):
    try:
        return puerta_models.actualizar_puerta(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/eliminar")
def eliminar_puerta(data: PuertaDelete):
    try:
        return puerta_models.eliminar_puerta(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/listar")
def listar_puertas():
    try:
        return puerta_models.obtener_puertas()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/nivel/{id_nivel}")
def puertas_por_nivel(id_nivel: int):
    try:
        return puerta_models.obtener_puertas_por_nivel(id_nivel)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
