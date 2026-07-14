from ta.momentum import RSIIndicator
from ta.trend import SMAIndicator
from ta.trend import MACD

from ta.momentum import RSIIndicator
from ta.trend import SMAIndicator, MACD


def calculate_indicators(data):

    close = data["Close"].squeeze()
    volume = data["Volume"].squeeze()

    rsi = RSIIndicator(close).rsi().iloc[-1]

    sma50 = SMAIndicator(close, window=50).sma_indicator().iloc[-1]
    sma200 = SMAIndicator(close, window=200).sma_indicator().iloc[-1]

    macd = MACD(close)

    macd_value = macd.macd().iloc[-1]
    signal_value = macd.macd_signal().iloc[-1]

    avg_volume = volume.tail(20).mean()
    current_volume = volume.iloc[-1]

    return {
        "rsi": float(rsi),
        "sma50": float(sma50),
        "sma200": float(sma200),
        "macd": float(macd_value),
        "macd_signal": float(signal_value),
        "volume_ratio": float(current_volume / avg_volume)
    }


    