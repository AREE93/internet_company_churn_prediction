from fastapi.testclient import TestClient

from api.main import app


client = TestClient(app)


VALID_CUSTOMER = {
    "customerID": "TEST001",
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "BeginDate": "2019-02-01",
    "MultipleLines": "No",
    "InternetService": "DSL",
    "OnlineSecurity": "No",
    "OnlineBackup": "Yes",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "Yes",
    "StreamingMovies": "No",
    "Type": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 70.5,
    "TotalCharges": "846.0"
}


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_predict_valid_customer():
    response = client.post(
        "/predict",
        json=VALID_CUSTOMER
    )

    assert response.status_code == 200

    data = response.json()

    assert "churn_predicho" in data
    assert "probabilidad_churn" in data

    assert data["churn_predicho"] in [0, 1]
    assert 0 <= data["probabilidad_churn"] <= 1


def test_predict_missing_field():
    customer = VALID_CUSTOMER.copy()

    del customer["BeginDate"]

    response = client.post(
        "/predict",
        json=customer
    )

    assert response.status_code == 422


def test_predict_invalid_category():
    customer = VALID_CUSTOMER.copy()

    customer["InternetService"] = "pizza"

    response = client.post(
        "/predict",
        json=customer
    )

    assert response.status_code == 422
