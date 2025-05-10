from pydantic import BaseModel
from typing import Optional

class RolBase(BaseModel):
    id_empresa: int
    nombre: str
    usuario_creacion: str  # Usuario como string

class RolUpdate(BaseModel):
    id_rol: int
    id_empresa: int
    nombre: str
    usuario_actualizacion: str  # Usuario como string

class RolDelete(BaseModel):
    id_rol: int
    usuario_actualizacion: str  # Usuario como string

class RolOut(BaseModel):
    id_rol: int
    id_empresa: int
    nombre: str
    estado: int
    fecha_creacion: Optional[str]  # Fecha como string
    usuario_creacion: Optional[str]  # Usuario como string
    fecha_actualizacion: Optional[str]  # Fecha como string
    usuario_actualizacion: Optional[str]  # Usuario como string
