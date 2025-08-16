import pytest
from cli import run_interactive

@pytest.fixture
def mock_api_key(monkeypatch):
    monkeypatch.setenv("OPENWEATHER_API_KEY", "dummy_key")

def test_interactive_weather(monkeypatch, capsys, mock_api_key):
    inputs = iter(["1", "Delhi", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    monkeypatch.setattr("weather_utils.weather.Weather.get_weather", lambda self, city: print(f"Mocked weather for {city}"))
    with pytest.raises(SystemExit):  # because it calls exit()
        run_interactive()

    captured = capsys.readouterr()
    assert "Mocked weather for Delhi" in captured.out
