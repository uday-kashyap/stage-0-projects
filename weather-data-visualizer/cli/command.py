import argparse
from utils.config import get_api_key
from weather_utils import Weather, Forecast
import sys
from utils.logger_config import get_logger

# Setup log file
logger = get_logger("cli")


def run_command_mode() -> None:
    """
    Enable command line functionality for fetching weather info.

    """

    logger.info("Running in CLI mode")

    api_key = get_api_key()

    parser = argparse.ArgumentParser(description="Weather Report using OpenWeatherAPI")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--weather", action="store_true", help="Show current weather")
    group.add_argument("--forecast", action="store_true", help="Show forecast")

    parser.add_argument("--city", required=True, help="Name of the city")
    parser.add_argument(
        "--type",
        choices=["temperature", "humidity"],
        default="temperature",
        help="Type of forecast to display (only with --forecast)",
    )
    args = parser.parse_args()

    # Ensure --type is only valid if --forecast is specified
    if "--type" in sys.argv and not args.forecast:
        logger.warning("Invalid usage: --type used without --forecast")
        parser.error("--type is only valid with --forecast")

    # Default behaviour when the type of weather information is not specified
    if not (args.weather or args.forecast):
        logger.info("No specific mode passed. Defaulting to current weather.")
        args.weather = True
    try:
        if args.forecast:
            logger.info(
                f"Getting forecast for city '{args.city}' with type '{args.type}'"
            )
            forecast = Forecast(api_key, log_mode="cli")
            forecast.plot_forecast(args.city, args.type)
        if args.weather:
            logger.info(f"Getting current weather for city '{args.city}'")
            weather = Weather(api_key, log_mode="cli")
            weather.get_weather(args.city)

        logger.info("Returned from the CLI mode")

    except Exception:
        logger.exception(
            f"Unexpected error occurred while processing city '{args.city}'"
        )
        print(
            "❌ Something went wrong while processing your request. Please try again later."
        )
