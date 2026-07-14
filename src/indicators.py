from ta.momentum import RSIIndicator
from ta.trend import SMAIndicator


def calculate_indicators(close):

    rsi = RSIIndicator(close).rsi().iloc[-1]

    sma50 = SMAIndicator(close, window=50).sma_indicator().iloc[-1]

    sma200 = SMAIndicator(close, window=200).sma_indicator().iloc[-1]

    return {
        "rsi": float(rsi),
        "sma50": float(sma50),
        "sma200": float(sma200)
    }