from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    redis_url: str = "redis://redis:6379"
    opendota_api_key: str = ""
    steam_api_key: str = ""
    debug: bool = False

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
