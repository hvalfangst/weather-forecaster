from pydantic import HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    weather_forecast_api_url: HttpUrl
    user_agent: str


settings = Settings()  # type: ignore[call-arg]
