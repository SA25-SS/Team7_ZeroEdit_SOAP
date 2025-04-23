# secrets.py
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load .env file
load_dotenv()

class Settings(BaseSettings):
    SOAP_SERVICE_URL: str
    SOAP_AUTH_URL: str

    class Config:
        env_file = ".env"

# Instantiate the settings
settings = Settings()
