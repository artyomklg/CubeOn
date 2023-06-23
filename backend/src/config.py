from typing import List

from pydantic import BaseSettings

from .constants import Environment


class Config(BaseSettings):
    # database
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    # auth
    SECRET: str
    ALGORITM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 20
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30
    ENVIRONMENT: Environment = Environment.PRODUCTION

    # keycloak
    KEYCLOAK_USER: str
    KEYCLOAK_PASSWORD: str
    KEYCLOAK_URL: str
    KEYCLOAK_CLIENT: str
    KEYCLOAK_REALM: str
    KEYCLOAK_CLIENT_SECRET: str
    KEYCLOAK_ADMIN_SECRET: str

    # corsmiddleware
    CORS_ORIGINS: List[str]
    CORS_HEADERS: List[str]
    CORS_METHODS: List[str]

    @property
    def Database_URL(self):
        return f'postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}'

    class Config:
        env_file = '.env'


settings = Config()

if __name__ == '__main__':
    print(settings.dict())
