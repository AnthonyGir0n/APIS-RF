from typing import Dict, Any, List
from pydantic import BaseModel

# Esquema para la solicitud de análisis facial
class ImageRequest(BaseModel):
    image: str  # Base64 encoded image

# Esquema para la solicitud de comparación facial
class FaceComparisonRequest(BaseModel):
    image1: str  # Base64 encoded image
    image2: str  # Base64 encoded image

# Esquema para la respuesta genérica
class Response(BaseModel):
    status: int
    data: Dict[str, Any]
    message: str