from pathlib import Path

from pydantic import BaseSettings

BASE_DIR = Path(__file__).parent


class Settings(BaseSettings):
    cluster_file: Path = BASE_DIR / "ad_targeter" / "data" / "countries.csv"


config = Settings()
