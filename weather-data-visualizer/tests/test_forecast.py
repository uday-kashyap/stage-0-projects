import pytest
import requests
from weather_utils import Forecast

@pytest.fixture
def sample_forecast_data():
    return {
        "list": [
            {"dt_txt": "2025-08-02 12:00:00", "main": {"temp": 30.2, "humidity": 56}},
            {"dt_txt": "2025-08-02 15:00:00", "main": {"temp": 31.1, "humidity": 52}},
            {"dt_txt": "2025-08-02 18:00:00", "main": {"temp": 29.8, "humidity": 60}},
            {"dt_txt": "2025-08-02 21:00:00", "main": {"temp": 28.5, "humidity": 65}},
        ]
    }

class MockResponse:
    def __init__(self, data=None, status_code=200):
        self._data = data or {}
        self.status_code = status_code

    def json(self):
        return self._data

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"{self.status_code} Error")


def test_get_forecast_temperature(monkeypatch, sample_forecast_data):
    def mock_get(*args, **kwargs):
        return MockResponse(sample_forecast_data, 200)

    monkeypatch.setattr(requests, "get", mock_get)

    forecast = Forecast(api_key="dummy")
    timestamps, values = forecast.get_forecast("Delhi", "temperature")

    assert len(timestamps) == 4
    assert values == [30.2, 31.1, 29.8, 28.5]


def test_get_forecast_humidity(monkeypatch, sample_forecast_data):
    def mock_get(*args, **kwargs):
        return MockResponse(sample_forecast_data, 200)

    monkeypatch.setattr(requests, "get", mock_get)

    forecast = Forecast(api_key="dummy")
    timestamps, values = forecast.get_forecast("Delhi", "humidity")

    assert values == [56, 52, 60, 65]


def test_extract_data_downsampling():
    forecast = Forecast(api_key="dummy")
    timestamps = [
        "2025-08-02 12:00:00",
        "2025-08-02 15:00:00",
        "2025-08-02 18:00:00",
        "2025-08-02 21:00:00",
        "2025-08-03 00:00:00",
    ]
    values = [30.2, 31.1, 29.8, 28.5, 27.0]

    new_ts, new_vals = forecast.extract_data(timestamps, values)

    assert len(new_ts) == 2  # SAMPLE_EVERY = 4
    assert new_vals == [30.2, 27.0]
