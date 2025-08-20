import pytest
import requests
from weather_utils import Weather


@pytest.fixture
def sample_weather_data():
    return {
        "name": "Delhi",
        "sys": {"country": "IN"},
        "main": {"temp": 33.5, "feels_like": 36.1, "humidity": 62},
        "weather": [{"description": "clear sky"}],
    }


def test_get_weather_success(monkeypatch, sample_weather_data, capsys):
    def mock_get(*args, **kwargs):
        class MockResponse:
            def __init__(self):
                self.status_code = 200

            def json(self):
                return sample_weather_data

            def raise_for_status(self):
                if self.status_code >= 400:
                    raise requests.HTTPError(f"{self.status_code} Error")

        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    weather = Weather(api_key="fake_api_key")
    weather.display_weather("Delhi")

    captured = capsys.readouterr()
    assert "Weather Report: Delhi(IN)" in captured.out
    assert "Temperature: 33.5°C" in captured.out


def test_get_weather_failure(monkeypatch, capsys):
    def mock_get(*args, **kwargs):
        class MockResponse:
            def __init__(self):
                self.status_code = 404

            def json(self):
                return {"message": "city not found"}

            def raise_for_status(self):
                if self.status_code >= 400:
                    raise requests.HTTPError(f"{self.status_code} Error")

        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    weather = Weather(api_key="fake_api_key")
    weather.display_weather("Nowhere")

    captured = capsys.readouterr()
    assert "Could not fetch weather data. Please check the city name." in captured.out
