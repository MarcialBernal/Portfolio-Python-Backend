import os
import joblib
import pandas as pd
from datetime import date, timedelta
from services.auto_ml.pipeline.train import train_model, save_model

# ============================================================
#                   PATHS
# ============================================================

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "model.pkl")
PROCESSED_DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "processed", "btc_daily.csv")


# ============================================================
#                   HELPERS
# ============================================================

def dataset_is_stale(df: pd.DataFrame, max_days: int = 10) -> bool:
    last_date = pd.to_datetime(df["date"].iloc[-1]).date()
    today = date.today()
    return (today - last_date).days > max_days


# ============================================================
#                   PREDICTION
# ============================================================

def predict_next_day():
    df = pd.read_csv(PROCESSED_DATA_PATH)

    # Auto retrain if data is stale
    if dataset_is_stale(df):
        print("Dataset is stale. Retraining model...")
        model, acc = train_model()
        save_model(model, acc)
    else:
        model = joblib.load(MODEL_PATH)

    last_return = df["return_pct"].iloc[-1]
    X = pd.DataFrame([[last_return]], columns=["return_pct"])

    proba = model.predict_proba(X)[0]
    pred = int(model.predict(X)[0])

    tomorrow = date.today() + timedelta(days=1)

    return {
        "date": tomorrow.isoformat(),
        "trend": "UP" if pred == 1 else "DOWN",
        "confidence": float(max(proba))
    }


# ============================================================
#                   ENTRY POINT
# ============================================================

if __name__ == "__main__":
    print(predict_next_day())
