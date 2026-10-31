from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.api.routes import audio, process, projects

app = FastAPI(
    title=settings.APP_NAME,
    description="World-class vocal processing with Persian/Dastgah music support",
    version=settings.VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(audio.router, prefix="/api/audio", tags=["audio"])
app.include_router(process.router, prefix="/api/process", tags=["process"])
app.include_router(projects.router, prefix="/api/projects", tags=["projects"])


@app.get("/health")
async def health():
    return {"status": "ok", "version": settings.VERSION}


@app.get("/")
async def root():
    return {"message": "FreeVoice Pro API", "docs": "/docs"}
