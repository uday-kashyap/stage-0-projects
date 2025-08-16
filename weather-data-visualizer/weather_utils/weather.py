import requests
from utils.logger_config import get_logger


class Weather:

    def __init__(self, api_key, log_mode=None):
        self.API_KEY = api_key
        self.logger = get_logger(log_mode)

    def get_weather(self, city: str) -> None:
        """
        Fetch and display real-time weather information for a given city.

        Parameters:
            city (str): Name of the city for which weather data is to be fetched.

        Returns:
            None: Prints temperature, condition, humidity, and feels-like temperature.
        """

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.API_KEY}&units=metric"

        try:
            response = requests.get(url)
            response.raise_for_status()

            # Fetch data from the server
            self.logger.info(f"Fetching data for the city '{city}'")
            data = response.json()

            # Define weather attributes
            city_name = data["name"]
            country_code = data["sys"]["country"]
            temperature = data["main"]["temp"]
            condition = data["weather"][0]["description"].title()
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]

            print(f"Weather Report: {city_name}({country_code})")
            print(f"Temperature: {temperature}°C")
            print(f"Condition: {condition}")
            print(f"Feels Like: {feels_like}°C")
            print(f"Humidity: {humidity} %")
            self.logger.info(
                f"Displayed the current weather data for the city '{city}' successfully!"
            )

        except requests.exceptions.HTTPError as e:
            self.logger.error(f"HTTP error occurred: {e}")
            print("Could not fetch weather data. Please check the city name.")

        except requests.exceptions.RequestException as e:
            self.logger.error(f"Request failed: {e}")
            print("Network error occurred. Please check your internet connection.")

        except KeyError as e:
            self.logger.error(f"Unexpected response format: Missing key {e}")
            print("Unexpected error. Please try again later.")
