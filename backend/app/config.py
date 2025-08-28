from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    APP_NAME: str = "MultiProviderChat"
    APP_ENV: str = "dev"
    APP_DEBUG: bool = True

    CORS_ORIGINS: str = "http://localhost:3000"

    # Database
    DATABASE_URL: str

    # Auth
    JWT_SECRET: str
    JWT_EXPIRE_SECONDS: int = 86400

    # LLM Providers
    OPENAI_API_KEY: str | None = None
    ANTHROPIC_API_KEY: str | None = None
    GEMINI_API_KEY: str | None = None

    # Defaults
    DEFAULT_PROVIDER: str = "openai"
    DEFAULT_MODEL: str = "gpt-3.5-turbo"

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), "..", ".env")
        env_file_encoding = "utf-8"

# Load settings
settings = Settings()
