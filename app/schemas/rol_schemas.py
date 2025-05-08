from pydantic import BaseModel
from typing import Optional

class RolBase(BaseModel):
    id_empresa: int
    nombre: str
    usuario_creacion: str

class RolUpdate(BaseModel):
    id_rol: int
    id_empresa: int
    nombre: str
    usuario_actualizacion: str

class RolDelete(BaseModel):
    id_rol: int
    usuario_actualizacion: str

class RolOut(BaseModel):
    id_rol: int
    id_empresa: int
    nombre: str
    estado: int
    fecha_creacion: Optional[str]
    usuario_creacion: Optional[str]
    fecha_actualizacion: Optional[str]
    usuario_actualizacion: Optional[str]
