import yfinance as yf
from datetime import datetime
from ta.momentum import RSIIndicator
from ta.trend import SMAIndicator


WATCHLIST = {
    "Amazon": "AMZN",
    "Telekom": "DTE.DE",
    "Kontron": "KTN.DE",
    "Veolia": "VIE.PA",
    "Viking Therapeutics": "VKTX",
    "Akebia Therapeutics": "AKBA"
}


def analyze_stock(ticker):

    data = yf.download(
        ticker,
        period="1y",
        progress=False
    )

    if data.empty:
        return None

    close = data["Close"].squeeze()

    # Indikatoren
    rsi = RSIIndicator(close).rsi().iloc[-1]

    sma50 = SMAIndicator(
        close,
        window=50
    ).sma_indicator().iloc[-1]

    sma200 = SMAIndicator(
        close,
        window=200
    ).sma_indicator().iloc[-1]

    kurs = close.iloc[-1]

    score = 50

    # RSI Bewertung
    if rsi < 30:
        score += 20
    elif rsi < 40:
        score += 10
    elif rsi > 70:
        score -= 10

    # Trend
    if kurs > sma50:
        score += 15

    if kurs > sma200:
        score += 15

    score = max(0, min(score, 100))


    if score >= 80:
        signal = "🟢 Kaufen"
    elif score >= 60:
        signal = "🟡 Beobachten"
    else:
        signal = "🔴 Abwarten"


    return {
        "kurs": round(float(kurs),2),
        "rsi": round(float(rsi),1),
        "score": score,
        "signal": signal
    }



html = f"""
<!DOCTYPE html>
<html lang="de">

<head>
<meta charset="UTF-8">

<title>SignalBot Dashboard</title>

<style>

body {{
font-family: Arial;
margin:40px;
}}

table {{
width:100%;
border-collapse:collapse;
}}

th,td {{
padding:12px;
border-bottom:1px solid #ddd;
}}

</style>

</head>

<body>


<h1>📈 SignalBot Dashboard</h1>

<p>
Aktualisiert:
{datetime.now().strftime("%d.%m.%Y %H:%M")}
</p>


<table>

<tr>
<th>Aktie</th>
<th>Kurs</th>
<th>RSI</th>
<th>Score</th>
<th>Signal</th>
</tr>

"""


for name, ticker in WATCHLIST.items():

    result = analyze_stock(ticker)

    if result:

        html += f"""

<tr>

<td>{name}</td>

<td>{result['kurs']}</td>

<td>{result['rsi']}</td>

<td>{result['score']}</td>

<td>{result['signal']}</td>

</tr>

"""


html += """

</table>

</body>

</html>

"""


with open(
    "docs/index.html",
    "w",
    encoding="utf-8"
) as file:

    file.write(html)


print("✅ Dashboard aktualisiert")