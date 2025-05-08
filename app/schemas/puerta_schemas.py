from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PuertaBase(BaseModel):
    id_nivel: int
    nombre: str

class PuertaCreate(PuertaBase):
    usuario_creacion: str

class PuertaUpdate(PuertaBase):
    id_puerta: int
    usuario_actualizacion: str

class PuertaDelete(BaseModel):
    id_puerta: int
    usuario_actualizacion: str

class PuertaOut(PuertaBase):
    id_puerta: int
    estado: int
    fecha_creacion: Optional[datetime]
    usuario_creacion: Optional[str]
    fecha_actualizacion: Optional[datetime]
    usuario_actualizacion: Optional[str]
