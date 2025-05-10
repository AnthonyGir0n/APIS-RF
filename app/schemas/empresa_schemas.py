from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EmpresaBase(BaseModel):
    nombre: str

class EmpresaCreate(EmpresaBase):
    usuario_creacion: str
    fecha_creacion: datetime
    estado: int

class EmpresaUpdate(EmpresaBase):
    usuario_actualizacion: str
    
class EmpresaDelete(BaseModel):
    usuario_actualizacion: str

class EmpresaOut(EmpresaBase):
    id_empresa: int
    estado: int
    fecha_creacion: Optional[datetime]
    usuario_creacion: Optional[str]
    fecha_actualizacion: Optional[datetime]
    usuario_actualizacion: Optional[str]