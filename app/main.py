from fastapi import FastAPI
from app.schemas import CustomerInput
from src.predict import predict_customer

app = FastAPI(title="Customer Segmentation API")


@app.get("/")
def home():
    return {"message": "API is running"}


@app.post("/predict")
def predict(data: CustomerInput):
    result = predict_customer(data)
    return {
        "segment": result
    }  