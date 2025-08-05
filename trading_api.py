
import requests
import config

def execute_trade(trade_details):
    """
    Executes a trade on OANDA.
    """
    if not trade_details:
        return

    url = f"{config.OANDA_API_URL}/v3/accounts/{config.OANDA_ACCOUNT_ID}/orders"
    headers = {
        "Authorization": f"Bearer {config.OANDA_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "order": {
            "instrument": trade_details['instrument'],
            "units": trade_details['units'],
            "type": "MARKET",
            "positionFill": "DEFAULT",
            "stopLossOnFill": {
                "price": str(trade_details['stop_loss'])
            },
            "takeProfitOnFill": {
                "price": str(trade_details['take_profit'])
            }
        }
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        print(f"Trade executed successfully: {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Error executing trade: {e}")
