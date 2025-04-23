from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    oc_api_url: str
    oc_api_host: str
    oc_api_key: str

    class Config:
        env_file= ".env"

settings = Settings()
