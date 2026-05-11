from datetime import datetime

import pytest
import responses

from weather_forecast.api import call_api_and_save_json

API_URL = "https://api.met.no/weatherapi/locationforecast/2.0/complete?lat=59.91&lon=10.75"


@responses.activate
def test_call_api_success_writes_file(chdir_tmp, sample_forecast_data):
    responses.add(responses.GET, API_URL, json=sample_forecast_data, status=200)
    (chdir_tmp / "forecasts").mkdir()

    result = call_api_and_save_json(API_URL)

    expected = f"forecasts/{datetime.now().date()}.json"
    assert result == expected
    written = (chdir_tmp / expected).read_text()
    assert '"air_temperature"' in written


@responses.activate
def test_call_api_403_exits(chdir_tmp):
    responses.add(responses.GET, API_URL, status=403)
    (chdir_tmp / "forecasts").mkdir()

    with pytest.raises(SystemExit) as exc_info:
        call_api_and_save_json(API_URL)
    assert exc_info.value.code == 1


@responses.activate
def test_call_api_skips_when_file_exists(chdir_tmp):
    forecasts = chdir_tmp / "forecasts"
    forecasts.mkdir()
    existing = forecasts / f"{datetime.now().date()}.json"
    existing.write_text('{"cached": true}')

    result = call_api_and_save_json(API_URL)

    assert result == f"forecasts/{datetime.now().date()}.json"
    assert existing.read_text() == '{"cached": true}'
    assert len(responses.calls) == 0
