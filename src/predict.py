import joblib
import numpy as np
from core.config import MODEL_PATH, SCALER_PATH, CLUSTER_NAMES

# Load artifacts
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
cluster_names = joblib.load(CLUSTER_NAMES)


def predict_customer(data):
    """
    Predict customer segment
    """

    # 🔹 Validation (moved from utils)
    if not (0 < data.age <= 120):
        raise ValueError("Age must be between 1 and 120")

    if data.income < 0:
        raise ValueError("Income cannot be negative")

    if not (0 <= data.spending <= 100):
        raise ValueError("Spending must be between 0 and 100")

    # 🔹 Format input
    input_array = np.array([[data.age, data.income, data.spending]])

    # 🔹 Scale
    scaled = scaler.transform(input_array)

    # 🔹 Predict
    cluster = model.predict(scaled)[0]

    # 🔹 Map label
    return cluster_names.get(cluster, "Unknown") 
