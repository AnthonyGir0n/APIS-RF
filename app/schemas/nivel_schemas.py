from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class NivelBase(BaseModel):
    id_nivel: int
    id_edificio: int
    nombre: str

class NivelCreate(NivelBase):
    usuario_creacion: str

class NivelUpdate(NivelBase):
    usuario_actualizacion: str
    
class NivelDelete(BaseModel):
    usuario_actualizacion: str

class NivelOut(NivelBase):
    estado: int
    fecha_creacion: Optional[datetime]
    usuario_creacion: Optional[str]
    fecha_actualizacion: Optional[datetime]
    usuario_actualizacion: Optional[str]