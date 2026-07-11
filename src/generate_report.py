import yfinance as yf
from datetime import datetime


WATCHLIST = {
    "Amazon": "AMZN",
    "Telekom": "DTE.DE",
    "Kontron": "KTN.DE",
    "Veolia": "VIE.PA",
    "Viking Therapeutics": "VKTX",
    "Akebia Therapeutics": "AKBA"
}


def get_price(ticker):
    data = yf.Ticker(ticker)
    history = data.history(period="5d")

    if history.empty:
        return None

    return round(history["Close"].iloc[-1], 2)


html = f"""
<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<title>SignalBot Dashboard</title>

<style>
body {{
    font-family: Arial;
    margin: 40px;
}}

table {{
    width:100%;
    border-collapse:collapse;
}}

td, th {{
    padding:10px;
    border-bottom:1px solid #ddd;
}}

</style>

</head>

<body>

<h1>📈 SignalBot Dashboard</h1>

<p>Aktualisiert: {datetime.now().strftime("%d.%m.%Y %H:%M")}</p>

<table>

<tr>
<th>Aktie</th>
<th>Ticker</th>
<th>Kurs</th>
</tr>

"""


for name, ticker in WATCHLIST.items():

    kurs = get_price(ticker)

    html += f"""
<tr>
<td>{name}</td>
<td>{ticker}</td>
<td>{kurs}</td>
</tr>
"""


html += """

</table>

</body>
</html>
"""


with open("docs/index.html", "w", encoding="utf-8") as file:
    file.write(html)


print("Dashboard aktualisiert!")