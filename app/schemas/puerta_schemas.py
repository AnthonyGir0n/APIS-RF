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
    fecha_creacion: Optional[str]  # Fecha como string
    usuario_creacion: Optional[str]  # Usuario como string
    fecha_actualizacion: Optional[str]  # Fecha como string
    usuario_actualizacion: Optional[str]  # Usuario como string
