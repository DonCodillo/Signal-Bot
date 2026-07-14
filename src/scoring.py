def calculate_score(price, indicators):

    score = 50

    # RSI
    if indicators["rsi"] < 30:
        score += 20
    elif indicators["rsi"] < 40:
        score += 10
    elif indicators["rsi"] > 70:
        score -= 10

    # Trend
    if price > indicators["sma50"]:
        score += 15

    if price > indicators["sma200"]:
        score += 15

    # MACD
    if indicators["macd"] > indicators["macd_signal"]:
        score += 10

    # Volumen
    if indicators["volume_ratio"] > 1.2:
        score += 5

    score = max(0, min(score, 100))

    if score >= 85:
        signal = "🟢 Stark Kaufen"
    elif score >= 70:
        signal = "🟢 Kaufen"
    elif score >= 55:
        signal = "🟡 Beobachten"
    else:
        signal = "🔴 Abwarten"

    return score, signal