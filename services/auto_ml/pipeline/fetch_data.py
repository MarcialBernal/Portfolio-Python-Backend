import os
import requests
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

# ============================================================
#                   CONFIG
# ============================================================

COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY")
BASE_URL = "https://api.coingecko.com/api/v3"
RAW_DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "raw", "btc_raw.csv")


# ============================================================
#                   DATA FETCHING
# ============================================================

def fetch_btc_market_data(days: int = 365):
    url = f"{BASE_URL}/coins/bitcoin/market_chart"
    params = {
        "vs_currency": "usd",
        "days": days
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    data = response.json()
    prices = data["prices"]

    df = pd.DataFrame(prices, columns=["timestamp", "price"])
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
    df = df[["date", "price"]]

    return df


# ============================================================
#                   SAVE
# ============================================================

def save_raw_data(df: pd.DataFrame):
    os.makedirs(os.path.dirname(RAW_DATA_PATH), exist_ok=True)
    df.to_csv(RAW_DATA_PATH, index=False)
    print(f"Raw BTC data saved to {RAW_DATA_PATH}")


# ============================================================
#                   ENTRY POINT
# ============================================================

if __name__ == "__main__":
    df = fetch_btc_market_data()
    save_raw_data(df)
