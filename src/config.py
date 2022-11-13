from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "My Planner"
    MONGODB_CONNECTION_STRING: str
    DEBUG: bool = False

    class Config:
        env_file = "src/.env"
