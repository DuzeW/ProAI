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


class AttractionTool(BaseTool):
    name: str = "AttractionTool"
    description: str = "Provides information about attractions in a given city using Google Places API."
    api_key: str = os.getenv("GOOGLE_PLACES_API_KEY")

    def _get_city_coordinates(self, city: str):
        """Fetch coordinates for a city using Google Places API."""
        url = "https://maps.googleapis.com/maps/api/geocode/json"
        params = {
            "address": city,
            "key": self.api_key
        }

        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                if data.get("results"):
                    location = data["results"][0]["geometry"]["location"]
                    return location["lat"], location["lng"]
            logger.error("Failed to fetch city coordinates")
            return None, None
        except Exception as e:
            logger.error(f"Error while fetching city coordinates: {str(e)}")
            return None, None

    def _run(self, city: str) -> str:
        """Fetches attraction information for the given city using Google Places API."""
        if not self.api_key:
            return str({"error": "Missing API key for attractions"})

        lat, lon = self._get_city_coordinates(city)
        if lat is None or lon is None:
            return str({"error": f"Could not determine coordinates for {city}"})

        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        params = {
            "location": f"{lat},{lon}",
            "radius": 5000,
            "type": "tourist_attraction",
            "key": self.api_key
        }

        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                attractions = []

                for place in data.get("results", []):
                    attractions.append({
                        "attraction_name": place.get("name", "Unknown"),
                        "rating": place.get("rating", "No rating available"),
                        "address": place.get("vicinity", "No address available"),
                    })
                return str(attractions)
            else:
                return str({"error": "Failed to fetch attractions"})
        except Exception as e:
            logger.error(f"Error while fetching attractions: {str(e)}")
            return str({"error": "Error while fetching attraction information"})
