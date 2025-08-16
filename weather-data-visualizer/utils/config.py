import os
from dotenv import load_dotenv


# Load .env variables
def get_api_key():
    """
    Load the api key
    """
    load_dotenv()
    API_KEY = os.getenv("OPENWEATHER_API_KEY")
    if not API_KEY:
        raise ValueError("⚠️ OPENWEATHER_API_KEY not found in .env file.")
    return API_KEY
