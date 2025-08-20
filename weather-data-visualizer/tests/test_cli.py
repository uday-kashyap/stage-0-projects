import pytest
import sys
from cli import run_command_mode


@pytest.fixture
def mock_api_key(monkeypatch):
    monkeypatch.setenv("OPENWEATHER_API_KEY", "dummy_key")


def test_cli_weather(monkeypatch, capsys, mock_api_key):
    sys.argv = ["main.py", "--city", "Delhi", "--weather"]

    monkeypatch.setattr(
        "weather_utils.weather.Weather.get_weather",
        lambda self, city: print(f"Mocked weather for {city}"),
    )
    run_command_mode()

    captured = capsys.readouterr()
    assert "Mocked weather for Delhi" in captured.out


def test_cli_forecast(monkeypatch, capsys, mock_api_key):
    sys.argv = ["main.py", "--city", "Delhi", "--forecast", "--type", "humidity"]

    monkeypatch.setattr(
        "weather_utils.forecast.Forecast.plot_forecast",
        lambda self, city, ftype: print(f"Mocked forecast {ftype} for {city}"),
    )
    run_command_mode()

    captured = capsys.readouterr()
    assert "Mocked forecast humidity for Delhi" in captured.out
