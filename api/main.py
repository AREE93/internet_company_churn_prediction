from fastapi import FastAPI
import pandas as pd

from src.predict import predict_churn

app = FastAPI(
    title="Internet Company Churn Prediction API",
    description="API for predicting customer churn using LightGBM.",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Internet Company Churn Prediction API",
        "status": "running"
    }


@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])

    results = predict_churn(df)

    return {
        "churn_predicho": int(
            results["Churn_predicho"].iloc[0]
        ),
        "probabilidad_churn": float(
            results["Probabilidad_churn"].iloc[0]
        )
    }