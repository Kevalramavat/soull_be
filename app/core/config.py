from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Soull API"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"
    
    # Database Settings
    # Format: postgresql+asyncpg://user:password@host:port/dbname
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/soull_db"

    model_config = SettingsConfigDict(case_sensitive=True, env_file=".env")

settings = Settings()
