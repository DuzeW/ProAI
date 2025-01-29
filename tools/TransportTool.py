import requests
import os
import logging
from crewai.tools import BaseTool
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

class TransportTool(BaseTool):
    name: str = "TransportTool"
    description: str = "Provides information about available transportation options in a given city."
    api_key: str = os.getenv("GOOGLE_PLACES_API_KEY")

    def _run(self, city: str) -> str:
        """Fetches available transport modes in the given city."""
        if not self.api_key:
            return str({"error": "Missing API key for transportation"})

        transport_modes = {
            "Subway": "subway_station",
            "Bus": "bus_station",
            "Train": "train_station",
            "Taxi": "taxi_stand",
            "Tram": "light_rail_station",
            "Airport": "airport",
            "Car Rental": "car_rental",
            "Bicycle": "bicycle_store"
        }

        available_transport = []
        try:
            url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
            for mode, query in transport_modes.items():
                params = {
                    "query": f"{query} in {city}",
                    "key": self.api_key
                }
                response = requests.get(url, params=params)
                if response.status_code == 200 and response.json().get("results"):
                    available_transport.append(mode)
        except Exception as e:
            logger.error(f"Error while fetching transportation data: {str(e)}")
            return str({"error": "Error while fetching transportation options"})

        return str({"available_transport": available_transport})