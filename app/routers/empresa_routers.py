from fastapi import APIRouter, HTTPException
from app.schemas.empresa_schemas import EmpresaCreate, EmpresaUpdate, EmpresaDelete
from app.models import empresa_models

router = APIRouter(
    prefix="/empresas",
    tags=["Empresas"]
)

@router.post("/crear")
def crear_empresa(data: EmpresaCreate):
    try:
        return empresa_models.crear_empresa(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/actualizar")
def actualizar_empresa(data: EmpresaUpdate):
    try:
        return empresa_models.actualizar_empresa(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/eliminar")
def eliminar_empresa(data: EmpresaDelete):
    try:
        return empresa_models.eliminar_empresa(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/listar")
def listar_empresa():
    try:
        return empresa_models.obtener_empresas()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
