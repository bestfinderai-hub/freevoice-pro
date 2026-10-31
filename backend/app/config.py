from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    APP_NAME: str = "FreeVoice Pro"
    VERSION: str = "0.1.0"
    DEBUG: bool = False

    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "https://freevoice-pro.vercel.app",
    ]

    # Supabase
    SUPABASE_URL: str = ""
    SUPABASE_SERVICE_KEY: str = ""
    SUPABASE_ANON_KEY: str = ""

    # Audio limits
    MAX_AUDIO_SIZE_MB: int = 50
    MAX_AUDIO_DURATION_SEC: int = 600
    SUPPORTED_FORMATS: List[str] = ["wav", "mp3", "flac", "aiff", "ogg"]

    # Processing
    DEFAULT_SAMPLE_RATE: int = 44100
    HOP_LENGTH: int = 512

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
