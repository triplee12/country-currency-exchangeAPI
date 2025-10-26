from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    RESTCOUNTRIES_URL: str = 'https://restcountries.com/v2/all?fields=name,capital,region,population,flag,currencies'
    EXCHANGE_URL: str = 'https://open.er-api.com/v6/latest/USD'
    CACHE_DIR: str = 'cache'

    class Config:
        env_file = '.env'

@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
