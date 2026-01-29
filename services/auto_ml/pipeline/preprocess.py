import os
import pandas as pd

# ============================================================
#                   PATHS
# ============================================================

RAW_DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "raw", "btc_raw.csv")
PROCESSED_DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "processed", "btc_daily.csv")


# ============================================================
#                   PREPROCESSING
# ============================================================

def preprocess_btc_data():
    df = pd.read_csv(RAW_DATA_PATH, parse_dates=["date"])

    # Daily percentage return
    df["return_pct"] = df["price"].pct_change()

    # Trend label: 1 = next day goes up, 0 = down or equal
    df["trend"] = (df["return_pct"].shift(-1) > 0).astype(int)

    # Drop last row (no future label)
    df = df.dropna()

    return df


# ============================================================
#                   SAVE
# ============================================================

def save_processed_data(df: pd.DataFrame):
    os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH, index=False)
    print(f"Daily BTC data saved to {PROCESSED_DATA_PATH}")


# ============================================================
#                   ENTRY POINT
# ============================================================

if __name__ == "__main__":
    df = preprocess_btc_data()
    save_processed_data(df)
