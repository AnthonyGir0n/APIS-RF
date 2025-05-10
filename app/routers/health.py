from fastapi import APIRouter
from app.database import test_db_connection

router = APIRouter()

@router.get("/health", tags=["Healthy Check"])
def health_check():
    if test_db_connection():
        return {"status": "ok", "message": "Base de datos funcionando correctamente"}
    else:
        return {"status": "error", "message": "Base de datos no disponible"}
