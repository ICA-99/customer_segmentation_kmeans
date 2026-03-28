import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASET_PATH = os.path.join(BASE_DIR, "data", "store_customers.csv")

MODEL_PATH = os.path.join(BASE_DIR, "models", "model.joblib")
SCALER_PATH = os.path.join(BASE_DIR, "models", "scaler.joblib")
CLUSTER_NAMES = os.path.join(BASE_DIR, "models", "cluster_names.joblib")
