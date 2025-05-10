from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importar routers existentes
from app.routers import health, reconocimiento, puerta_routers, rol_routers, empresa_routers, edificio_routers, nivel_routers


app = FastAPI(
    title="API de Reconocimiento Facial",
    description="API para reconocimiento facial con Azure Face API",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(health.router)
app.include_router(reconocimiento.router)
app.include_router(puerta_routers.router)
app.include_router(rol_routers.router) 
app.include_router(empresa_routers.router)  
app.include_router(edificio_routers.router) 
app.include_router(nivel_routers.router)

# Ruta raíz opcional
@app.get("/")
def root():
    return {"message": "API de Reconocimiento Facial - OK"}
