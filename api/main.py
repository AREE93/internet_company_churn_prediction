
from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

from src.predict import predict_churn


app = FastAPI(
    title="Internet Company Churn Prediction API",
    description="API for predicting customer churn using LightGBM.",
    version="1.0.0"
)


class CustomerData(BaseModel):
    customerID: str

    gender: Literal[
        "Male",
        "Female"
    ]

    SeniorCitizen: int

    Partner: Literal[
        "Yes",
        "No"
    ]

    Dependents: Literal[
        "Yes",
        "No"
    ]

    BeginDate: str

    MultipleLines: Literal[
        "Yes",
        "No",
        "No phone service"
    ]

    InternetService: Literal[
        "DSL",
        "Fiber optic",
        "No"
    ]

    OnlineSecurity: Literal[
        "Yes",
        "No",
        "No internet service"
    ]

    OnlineBackup: Literal[
        "Yes",
        "No",
        "No internet service"
    ]

    DeviceProtection: Literal[
        "Yes",
        "No",
        "No internet service"
    ]

    TechSupport: Literal[
        "Yes",
        "No",
        "No internet service"
    ]

    StreamingTV: Literal[
        "Yes",
        "No",
        "No internet service"
    ]

    StreamingMovies: Literal[
        "Yes",
        "No",
        "No internet service"
    ]

    Type: Literal[
        "Month-to-month",
        "One year",
        "Two year"
    ]

    PaperlessBilling: Literal[
        "Yes",
        "No"
    ]

    PaymentMethod: Literal[
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]

    MonthlyCharges: float
    TotalCharges: str


@app.get("/")
def root():
    return {
        "message": "Internet Company Churn Prediction API",
        "status": "running"
    }


@app.post("/predict")
def predict(data: CustomerData):

    df = pd.DataFrame([
        data.model_dump()
    ])

    results = predict_churn(df)

    return {
        "churn_predicho": int(
            results["Churn_predicho"].iloc[0]
        ),
        "probabilidad_churn": float(
            results["Probabilidad_churn"].iloc[0]
        )
    }

