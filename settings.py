from os import environ
from pathlib import Path

from pydantic import BaseSettings

BASE_DIR = Path(__file__).parent


class Settings(BaseSettings):
    CLUSTER_FILE: Path = BASE_DIR / "ad_targeter" / "data" / "countries.csv"
    HOST: str = "127.0.0.1"
    PORT: int = 5000

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


config = Settings()
