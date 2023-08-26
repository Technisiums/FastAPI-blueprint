"""All general settings and env variables are done here"""

from dotenv import load_dotenv, find_dotenv
from pydantic_settings import BaseSettings


load_dotenv(find_dotenv())


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI: str = None


settings = Settings()

