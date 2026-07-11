import yfinance as yf

WATCHLIST = {
    "Amazon": "AMZN",
    "Telekom": "DTE.DE",
    "Kontron": "KTN.DE",
    "Veolia": "VIE.PA",
    "Viking": "VKTX",
    "Akebia": "AKBA"
}

print("SignalBot startet...\n")

for name, ticker in WATCHLIST.items():
    try:
        aktie = yf.Ticker(ticker)
        info = aktie.fast_info

        print(f"{name}")
        print(f"Ticker: {ticker}")
        print(f"Letzter Kurs: {info['lastPrice']:.2f}")
        print("-" * 40)

    except Exception as e:
        print(f"Fehler bei {name}: {e}")
    

