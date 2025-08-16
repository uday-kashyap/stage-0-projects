import requests
import matplotlib.pyplot as plt
from datetime import datetime
from utils.logger_config import get_logger


class Forecast:

    def __init__(self, api_key, log_mode=None):
        self.API_KEY = api_key
        self.logger = get_logger(log_mode)

    def extract_data(self, timestamps: list, values: list) -> tuple[list, list]:
        """
        Extract and downsample forecast attributes for plotting.

        """

        # Format parsed forcast time and temperature data
        SAMPLE_EVERY = 4
        formatted_timestamps = []

        self.logger.info("Downsampling the data values for the plot")
        for i in range(0, len(timestamps), SAMPLE_EVERY):
            formatted_timestamps.append(
                datetime.strptime(timestamps[i], "%Y-%m-%d %H:%M:%S")
            )
        new_timestamps = [
            timestamp.strftime("%d/%m/%Y\n%H:%M hrs")
            for timestamp in formatted_timestamps
        ]

        new_values = []
        for j in range(0, len(values), SAMPLE_EVERY):
            new_values.append(values[j])

        self.logger.info("Successfully downsampled. Ready for plotting!")
        return new_timestamps, new_values

    def get_forecast(self, city: str, type: str) -> tuple[list, list]:
        """
        Fetch the 5-day with 3-hour step forecast data

        """

        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={self.API_KEY}&units=metric"

        try:
            response = requests.get(url)
            response.raise_for_status()

            # Fetch data from the server
            self.logger.info(f"Fetching data for the city '{city}'")
            data = response.json()

            forecast_list = data["list"]

            timestamps = []
            values = []

            self.logger.info(
                f"Extracting 'timestamps' and '{type}' from the parsed data"
            )
            for entry in forecast_list:
                timestamps.append(entry["dt_txt"])  # time in 'YYYY-MM-DD HH:MM:SS'
                if type == "temperature":
                    values.append(entry["main"]["temp"])  # in Celsius
                if type == "humidity":
                    values.append(entry["main"]["humidity"])  # in %

            self.logger.info("Required data has been extracted successfully.")
            return timestamps, values

        except requests.exceptions.HTTPError as e:
            self.logger.error(f"HTTP error occurred: {e}")
            print("Could not fetch weather data. Please check the city name.")

        except requests.exceptions.RequestException as e:
            self.logger.error(f"Request failed: {e}")
            print("Network error occurred. Please check your internet connection.")

        except KeyError as e:
            self.logger.error(f"Unexpected response format: Missing key {e}")
            print("Unexpected error. Please try again later.")

    def plot_forecast(self, city: str, type: str) -> None:
        """
        Plot the 5-day forecast temperature of a given city

        """
        timestamps, values = self.get_forecast(city, type)

        if timestamps and values:

            # Downsample the values
            new_timestamps, new_values = self.extract_data(timestamps, values)

            plt.figure(figsize=(12, 6))
            colour_style = "red" if type == "temperature" else "blue"
            plt.plot(
                new_timestamps,
                new_values,
                color=colour_style,
                linestyle="-",
                marker="o",
            )
            for x, y in zip(new_timestamps, new_values):
                plt.annotate(
                    f"{y}°C" if type == "temperature" else f"{y}%",
                    xy=(x, y),
                    xytext=(0, 5),  # 10 pixels above
                    textcoords="offset points",
                    ha="center",
                    fontsize=9,
                    color="black",
                )
            plt.title(f"5-Day {type.title()} Forecast - {city.title()}")
            plt.xlabel("Timestamp")
            plt.ylabel(f"{type.title()}{'(°C)' if type=='temperature' else '(%)'}")
            plt.tight_layout()
            plt.show()
            self.logger.info("The graph has been plotted successfully!")
        else:
            self.logger.warning(
                f"No forecast data available to plot for city '{city}'."
            )
            print(
                f"❌ Could not generate forecast graph for '{city.title()}'. Please try again later."
            )
