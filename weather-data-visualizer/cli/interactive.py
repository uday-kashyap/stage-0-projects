from utils.config import get_api_key
from weather_utils import Weather, Forecast
from utils.logger_config import get_logger

# Setup log file
logger = get_logger("interactive")


def forecast_menu(forecast_obj: Forecast) -> None:
    """
    Display forecasting facilities

    """

    logger.info("Entered forecast menu")

    options = {1: "Temperature Plot", 2: "Humidity Plot", 3: "Main Menu"}
    while True:
        for key, value in options.items():
            print(f"{key}. {value}")
        try:
            choice = int(input("Enter your choice: "))
            if choice not in options:
                print("⚠️  Enter valid choice please!")
                continue
        except ValueError:
            print("⚠️  The input must be an integer only")
        else:
            if choice in [1, 2]:
                code = "temperature" if choice == 1 else "humidity"
                logger.info(f"Chose for {code} plotting")
                city_name = input("Enter city name: ")
                print("---------------------------------")
                forecast_obj.plot_forecast(city_name, code)
            if choice == 3:
                logger.info("Exiting forecast menu")
                return


def run_interactive() -> None:
    """
    Display the main menu with utilities
    """

    api_key = get_api_key()

    logger.info("Running in interactive mode")

    weather = Weather(api_key, log_mode="interactive")
    forecast = Forecast(api_key, log_mode="interactive")

    options = {1: "Weather Report", 2: "Weather Forecast", 3: "Exit"}

    while True:

        # Display the main menu with utilities
        for key, value in options.items():
            print(f"{key}. {value}")
        try:
            choice = int(input("Enter your choice: "))
            if choice not in options:
                print("⚠️  Enter valid choice please!")
                continue
        except ValueError:
            print("⚠️  The input must be an integer only")
        else:
            if choice == 1:
                city_name = input("Enter city name: ")
                print("---------------------------------")
                weather.get_weather(city_name)
                print("---------------------------------")
            if choice == 2:
                print("---------------------------------")
                forecast_menu(forecast)
                print("---------------------------------")
            if choice == 3:
                logger.info("Returned from the interactive mode")
                print("---------------------------------")
                exit("The program was terminated :)")
