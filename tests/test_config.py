import pytest
from pydantic import ValidationError

from weather_forecast.config import Settings


def test_settings_loads_from_env(monkeypatch):
    monkeypatch.setenv("WEATHER_FORECAST_API_URL", "https://api.met.no/forecast")
    monkeypatch.setenv("USER_AGENT", "test-app/0.1 test@example.com")

    settings = Settings(_env_file=None)

    assert str(settings.weather_forecast_api_url).startswith("https://api.met.no/forecast")
    assert settings.user_agent == "test-app/0.1 test@example.com"


def test_settings_missing_required_raises(monkeypatch):
    monkeypatch.delenv("WEATHER_FORECAST_API_URL", raising=False)
    monkeypatch.delenv("USER_AGENT", raising=False)

    with pytest.raises(ValidationError):
        Settings(_env_file=None)


def test_settings_invalid_url_raises(monkeypatch):
    monkeypatch.setenv("WEATHER_FORECAST_API_URL", "not-a-url")
    monkeypatch.setenv("USER_AGENT", "test-app/0.1 test@example.com")

    with pytest.raises(ValidationError):
        Settings(_env_file=None)
