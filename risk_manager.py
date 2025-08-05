
import config

def apply_risk_management(decision):
    """
    Applies risk management rules to a trading decision.
    """
    if not decision or decision['decision'] == "HOLD":
        return None

    # This is a simplified example. A real risk manager would be more complex.
    # It should calculate position size based on account balance and risk percentage.
    # For now, we'll use a fixed unit size.

    units = 1000  # Example unit size
    if decision['decision'] == "SELL":
        units = -units

    # This is also simplified. A real implementation would get the current price.
    # We will assume a placeholder price for now.
    current_price = 1.0800  # Placeholder price for EUR/USD

    if decision['decision'] == "BUY":
        stop_loss = current_price - (config.STOP_LOSS_PIPS * 0.0001)
        take_profit = current_price + (config.TAKE_PROFIT_PIPS * 0.0001)
    else:  # SELL
        stop_loss = current_price + (config.STOP_LOSS_PIPS * 0.0001)
        take_profit = current_price - (config.TAKE_PROFIT_PIPS * 0.0001)

    return {
        "instrument": decision['instrument'],
        "units": units,
        "stop_loss": stop_loss,
        "take_profit": take_profit
    }
