import json
from pathlib import Path

import pytest

SAMPLE_FORECAST_PATH = Path(__file__).parent / "data" / "sample_forecast.json"


@pytest.fixture
def sample_forecast_data():
    return json.loads(SAMPLE_FORECAST_PATH.read_text())


@pytest.fixture
def sample_forecast_file(tmp_path, sample_forecast_data):
    p = tmp_path / "forecast.json"
    p.write_text(json.dumps(sample_forecast_data))
    return p


@pytest.fixture
def chdir_tmp(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    return tmp_path
