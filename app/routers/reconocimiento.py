import os
from fastapi import APIRouter, HTTPException
from app.schemas.reconocimiento import ImageRequest, FaceComparisonRequest, Response  # Importar esquemas
from app.models.reconocimiento import (  # Importar funciones del modelo
    base64_to_image,
    detect_face,
    verify_single_face,
    verify_face_quality,
    calculate_face_similarity
)

router = APIRouter()

@router.post("/api/face/analyze", response_model=Response, tags=["Obtener Metadata"])
async def analyze_face(request: ImageRequest):
    image_path = None
    try:
        image_path = await base64_to_image(request.image)
        face_detection_result = await detect_face(image_path)
        single_face = verify_single_face(face_detection_result)
        verify_face_quality(single_face)
        response_data = {"isValid": True}
        return Response(status=200, data=response_data, message="Correcto")
    except Exception as e:
        return Response(status=400, data={}, message=str(e))
    finally:
        if image_path and os.path.exists(image_path):
            os.remove(image_path)

@router.post("/api/face/compare", response_model=Response, tags=["Comparar Metadata"])
async def compare_faces(request: FaceComparisonRequest):
    image_path1, image_path2 = None, None
    try:
        image_path1 = await base64_to_image(request.image1)
        image_path2 = await base64_to_image(request.image2)
        face_detection_result1 = await detect_face(image_path1)
        face_detection_result2 = await detect_face(image_path2)
        single_face1 = verify_single_face(face_detection_result1)
        single_face2 = verify_single_face(face_detection_result2)
        similarity = calculate_face_similarity(
            single_face1['faceLandmarks'], 
            single_face2['faceLandmarks']
        )
        threshold = 80.0
        is_same_person = similarity >= threshold
        response_data = {
            "isSamePerson": is_same_person,
            "similarity": float(similarity),
            "threshold": float(threshold)
        }
        return Response(status=200, data=response_data, message="Análisis completado")
    except Exception as e:
        return Response(status=400, data={}, message=str(e))
    finally:
        if image_path1 and os.path.exists(image_path1):
            os.remove(image_path1)
        if image_path2 and os.path.exists(image_path2):
            os.remove(image_path2)