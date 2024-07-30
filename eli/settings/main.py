from dotenv import load_dotenv
from pydantic_settings import BaseSettings

_VERSION = "2024.7.1"  # EDITED BY BUMPVER, NO TOUCH

load_dotenv()


class Settings(BaseSettings):
    API_GENAI: str
    MODEL_NAME: str = "gemini-1.5-pro"


settings = Settings()
