import requests
import pandas as pd

# Base URL for CoinGecko API
url = "https://api.coingecko.com/api/v3/coins/markets"

# Parameters for the request
params = {
    "vs_currency": "usd",  # Get prices in USD
    "order": "market_cap_desc",  # Sort by market cap
    "per_page": 10,  # Number of coins to fetch
    "page": 1,  # Page number
    "sparkline": "false"  # No sparkline data
}

# Make the request
response = requests.get(url, params=params)

# Check for successful response
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)

    # Select relevant columns
    selected_columns = [
        "id", "symbol", "name", "current_price", "market_cap", "market_cap_rank",
        "total_volume", "price_change_percentage_24h", "ath", "atl"
    ]

    df = df[selected_columns]
    print(df)
else:
    print("Error:", response.status_code)

# Export to csv
df.to_csv("top10_coins.csv", index=False)