from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EdificioBase(BaseModel):
    id_edificio: int
    id_empresa: int
    nombre: str
    
class EdificioCreate(EdificioBase):
    usuario_creacion: str

class EdificioUpdate(EdificioBase):
    usuario_actualizacion: str
    
class EdificioDelete(BaseModel):
    usuario_actualizacion: str

class EdificioOut(EdificioBase):
    estado: int
    fecha_creacion: Optional[datetime]
    usuario_creacion: Optional[str]
    fecha_actualizacion: Optional[datetime]
    usuario_actualizacion: Optional[str]