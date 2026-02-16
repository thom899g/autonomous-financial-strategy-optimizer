import os

class Settings:
    API_KEY = os.getenv("MARKET_API_KEY", "default_key")
    DATA_SOURCE = os.getenv("DATA_SOURCE", "api")  # 'api' or 'db'
    RISK_TOLERANCE = float(os.getenv("RISK_TOLERANCE", 0.05))
    STRATEGY_REFRESH_INTERVAL = int(os.getenv("STRATEGY_REFRESH_INTERVAL", 60*60))  # seconds
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    
    @classmethod
    def validate(cls):
        valid = True
        if not cls.API_KEY:
            valid = False
            print("API key is missing.")
        if cls.DATA_SOURCE not in ['api', 'db']:
            valid = False
            print("Invalid data source specified.")
        return valid

# Initialize settings
Settings().validate()