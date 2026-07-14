def calculate_score(price, indicators):

    score = 50

    if indicators["rsi"] < 30:
        score += 20
    elif indicators["rsi"] < 40:
        score += 10
    elif indicators["rsi"] > 70:
        score -= 10

    if price > indicators["sma50"]:
        score += 15

    if price > indicators["sma200"]:
        score += 15

    score = max(0, min(score, 100))

    if score >= 80:
        signal = "🟢 Kaufen"
    elif score >= 60:
        signal = "🟡 Beobachten"
    else:
        signal = "🔴 Abwarten"

    return score, signal