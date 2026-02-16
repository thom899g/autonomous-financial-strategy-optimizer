import logging
from typing import Dict, Optional
import requests

class MarketDataFetcher:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        
    def fetch_data(self) -> Optional[Dict]:
        """
        Fetches market data from the configured source.
        """
        try:
            if Settings.DATA_SOURCE == 'api':
                return self._fetch_from_api()
            elif Settings.DATA_SOURCE == 'db':
                # Placeholder for database fetching
                return None  # TODO: Implement DB integration
            
        except Exception as e:
            self.logger.error(f"Failed to fetch data: {str(e)}")
            raise

    def _fetch_from_api(self) -> Dict:
        """
        Fetches market data from the API.
        """
        params = {
            'api_key': Settings.API_KEY,
            'interval': "1D"
        }
        
        try:
            response = requests.get("https://marketdata.example.com", params=params)
            if response.status_code == 200:
                return response.json()
            self.logger.error(f"API request failed with status code: {response.status_code}")
            return None
            
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Request exception occurred: {str(e)}")
            return None