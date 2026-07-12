import json
import yfinance as yf


def load_watchlist():
    with open("watchlist.json", "r", encoding="utf-8") as file:
        return json.load(file)


def download_stock_data(ticker):
    data = yf.download(
        ticker,
        period="1y",
        progress=False,
        auto_adjust=True
    )

    if data.empty:
        return None

    return data