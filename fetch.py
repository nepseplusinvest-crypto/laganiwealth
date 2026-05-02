import requests
import json

url = "https://nepsealpha.com/trading/1/day"
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

try:
    res = requests.get(url, headers=headers, timeout=10)
    res.raise_for_status()  # error भए रोक्छ

    data = res.json()

    stocks = []

    for i in data:
        try:
            symbol = i.get("symbol", "")
            price = float(i.get("ltp", 0))
            change = float(i.get("percent_change", 0))

            stocks.append({
                "symbol": symbol,
                "price": price,
                "change": change
            })
        except:
            continue  # कुनै data बिग्रियो भने skip

    # Sorting
    gainers = sorted(stocks, key=lambda x: x["change"], reverse=True)[:10]
    losers  = sorted(stocks, key=lambda x: x["change"])[:10]

    output = {
        "all": stocks,
        "gainers": gainers,
        "losers": losers
    }

    # Save file
    with open("data.json", "w") as f:
        json.dump(output, f, indent=2)

    print("✅ Data updated successfully")

except Exception as e:
    print("❌ Error:", e)
