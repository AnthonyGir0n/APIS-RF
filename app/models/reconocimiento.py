import os
from typing import Any, Dict, List
import uuid
import base64
import tempfile
import numpy as np
from scipy.spatial import distance
from dotenv import load_dotenv
import httpx
from app.schemas.reconocimiento import ImageRequest, FaceComparisonRequest  # Importar esquemas

# Cargar variables de entorno
load_dotenv()

# Configuración de Azure Face API
FACE_API_KEY = os.getenv("FACE_API_KEY")
FACE_ENDPOINT = os.getenv("FACE_ENDPOINT")

# Función para calcular la similitud basada en landmarks faciales
def calculate_face_similarity(landmarks1: Dict[str, Any], landmarks2: Dict[str, Any]) -> float:
    key_points = ['pupilLeft', 'pupilRight', 'noseTip', 'mouthLeft', 'mouthRight']
    points1 = np.array([[landmarks1[point]['x'], landmarks1[point]['y']] for point in key_points])
    points2 = np.array([[landmarks2[point]['x'], landmarks2[point]['y']] for point in key_points])

    def normalize_points(points):
        eye_distance = distance.euclidean(points[0], points[1])
        center = np.mean(points, axis=0)
        return (points - center) / eye_distance

    norm_points1 = normalize_points(points1)
    norm_points2 = normalize_points(points2)
    point_distances = [distance.euclidean(p1, p2) for p1, p2 in zip(norm_points1, norm_points2)]
    avg_distance = np.mean(point_distances)
    similarity = float(max(0, 100 - (avg_distance * 100)))
    return similarity

# Función para convertir Base64 a imagen
async def base64_to_image(base64_data: str) -> str:
    if "," in base64_data:
        base64_data = base64_data.split(",")[1]
    image_bytes = base64.b64decode(base64_data)
    fd, temp_path = tempfile.mkstemp(suffix='.jpg')
    os.close(fd)
    with open(temp_path, 'wb') as f:
        f.write(image_bytes)
    return temp_path

# Función para detectar rostros con Azure Face API
async def detect_face(image_path: str) -> List[Dict[str, Any]]:
    with open(image_path, 'rb') as f:
        image_data = f.read()
    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': FACE_API_KEY
    }
    params = {
        'returnFaceId': 'false',
        'returnFaceLandmarks': 'true',
        'returnFaceAttributes': 'blur,exposure,glasses,headPose,occlusion',
        'detectionModel': 'detection_03'
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{FACE_ENDPOINT}/face/v1.0/detect",
            headers=headers,
            params=params,
            content=image_data
        )
    if response.status_code != 200:
        raise Exception(f"Error en el servicio de detección facial: {response.text}")
    return response.json()

# Función para verificar si hay un solo rostro
def verify_single_face(face_data: List[Dict[str, Any]]) -> Dict[str, Any]:
    if not face_data or len(face_data) == 0:
        raise Exception("No se detectó ningún rostro en la imagen")
    if len(face_data) > 1:
        raise Exception("Se detectaron múltiples rostros en la imagen. Solo se permite un rostro")
    return face_data[0]

# Función para verificar la calidad y visibilidad de los rasgos faciales
def verify_face_quality(face_data: Dict[str, Any]) -> bool:
    occlusion = face_data['faceAttributes']['occlusion']
    if occlusion['eyeOccluded'] or occlusion['foreheadOccluded'] or occlusion['mouthOccluded']:
        raise Exception("Rasgos faciales importantes están ocultos o cubiertos")
    blur = face_data['faceAttributes']['blur']['value']
    exposure = face_data['faceAttributes']['exposure']['value']
    if blur > 0.7:
        raise Exception("La imagen está demasiado borrosa")
    if exposure > 0.8 or exposure < 0.2:
        raise Exception("La imagen tiene problemas de exposición (demasiado brillante o demasiado oscura)")
    head_pose = face_data['faceAttributes']['headPose']
    if abs(head_pose['pitch']) > 25 or abs(head_pose['yaw']) > 25 or abs(head_pose['roll']) > 25:
        raise Exception("La posición de la cabeza no es frontal. Por favor, mire directamente a la cámara")
    return True