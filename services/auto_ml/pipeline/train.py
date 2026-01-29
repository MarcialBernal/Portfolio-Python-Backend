import os
import json
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib


# ============================================================
#                   PATHS
# ============================================================

PROCESSED_DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "processed", "btc_daily.csv")
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "model.pkl")
METRICS_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "metrics.json")


# ============================================================
#                   TRAINING
# ============================================================

def train_model():
    df = pd.read_csv(PROCESSED_DATA_PATH, parse_dates=["date"])

    X = df[["return_pct"]]
    y = df["trend"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    return model, acc


# ============================================================
#                   SAVE
# ============================================================

def save_model(model, accuracy: float):
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)

    joblib.dump(model, MODEL_PATH)

    with open(METRICS_PATH, "w") as f:
        json.dump({"accuracy": accuracy}, f, indent=4)

    print(f"Model saved to {MODEL_PATH}")
    print(f"Accuracy saved to {METRICS_PATH}")


# ============================================================
#                   ENTRY POINT
# ============================================================

if __name__ == "__main__":
    model, accuracy = train_model()
    save_model(model, accuracy)
