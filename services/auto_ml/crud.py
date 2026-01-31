from services.auto_ml.pipeline.predict import predict_next_day


# ============================================================
#                   SERVICES
# ============================================================

def get_prediction():
    return predict_next_day()
