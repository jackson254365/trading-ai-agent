
import requests
import config

def fetch_market_data(instrument=config.INSTRUMENT, timeframe=config.TIMEFRAME, count=50):
    """
    Fetches historical market data from OANDA.
    """
    url = f"{config.OANDA_API_URL}/v3/instruments/{instrument}/candles"
    headers = {
        "Authorization": f"Bearer {config.OANDA_API_KEY}"
    }
    params = {
        "granularity": timeframe,
        "count": count
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching market data: {e}")
        return None
