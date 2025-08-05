
import google.generativeai as genai
import config

def get_trading_decision(market_data):
    """
    Analyzes market data using an LLM and returns a trading decision.
    """
    if not market_data or 'candles' not in market_data:
        return None

    # Configure the Gemini API
    genai.configure(api_key=config.GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-pro')

    # Construct a prompt for the LLM
    prompt = f"""
    Analyze the following Forex market data for {config.INSTRUMENT} ({config.TIMEFRAME}) and provide a trading decision (BUY, SELL, or HOLD).

    Data:
    {market_data['candles']}

    Based on this data, what is the most logical trading action?
    Please respond with only one word: BUY, SELL, or HOLD.
    """

    try:
        response = model.generate_content(prompt)
        decision = response.text.strip().upper()
        if decision in ["BUY", "SELL", "HOLD"]:
            return {"decision": decision, "instrument": config.INSTRUMENT}
        else:
            print(f"Invalid decision from LLM: {decision}")
            return None
    except Exception as e:
        print(f"Error getting trading decision from LLM: {e}")
        return None
