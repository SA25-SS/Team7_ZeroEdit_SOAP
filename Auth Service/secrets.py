from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mongodb_connection_string: str
    mongodb_database: str
    secret_key: str
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()

