from typing import Any, Literal

import orjson
from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL

PROJECT_NAME = "DEMO"


class DBSettings(BaseSettings):
    HOST: str
    PORT: int = 5432
    USERNAME: str
    PASSWORD: str
    NAME: str
    OPTIONS: dict = {}

    model_config = SettingsConfigDict(env_prefix="DB_")

    @property
    def sync_dns(self) -> URL:
        return self._get_dsn("postgresql")

    @property
    def async_dns(self) -> URL:
        return self._get_dsn("postgresql+asyncpg")

    def _get_dsn(self, drivername: Literal["postgresql+asyncpg", "postgresql"]) -> URL:
        return URL.create(
            drivername=drivername,
            host=settings.DB.HOST,
            port=settings.DB.PORT,
            username=settings.DB.USERNAME,
            password=settings.DB.PASSWORD,
            database=settings.DB.NAME,
        )


class Settings(BaseSettings):
    ENVIRONMENT: str = "PROD"
    DB: DBSettings = DBSettings()


settings = Settings()
