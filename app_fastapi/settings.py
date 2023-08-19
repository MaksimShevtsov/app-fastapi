"""Fast api settings"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Doc string"""
    home_url: str = "/"


settings = Settings()
