
🇲🇽 Spanish | 🇺🇸 English


# Customer Churn Prediction — Internet Company


Machine Learning project to predict customer churn for a telecommunications company. The project covers an end-to-end workflow, from data analysis and processing to model training, evaluation, interpretation, REST API exposure, containerization, automated testing, and production deployment.

## 🚀 Production API

API deployed on Render:

https://internet-company-churn-prediction.onrender.com

Swagger UI:

https://internet-company-churn-prediction.onrender.com/docs

The API accepts customer information and returns a churn prediction together with its probability.

Example response
{
  "churn_predicho": 1,
  "probabilidad_churn": 0.9999956167096107
}


### 📌 Project Overview

The main objective is to develop a model capable of identifying customers at risk of leaving the service.

The project follows a complete Data Science, Machine Learning, and deployment workflow:

Data loading and preparation.
Data cleaning and validation.
Feature engineering.
Target variable definition.
Comparison of different models.
Evaluation using multiple metrics.
Selection and optimization of the final model.
Model interpretation.
Saving the trained model.
Development of a REST API with FastAPI.
Containerization with Docker.
Deployment on Render.


### 📊 Dataset

The project uses customer data from a telecommunications company.

The original variables include:

Demographic information.
Subscribed services.
Contract type.
Payment method.
Paperless billing.
Monthly charges.
Total charges.
Start date.
End date.
Target variable

The Churn variable is created from EndDate:

df["Churn"] = df["EndDate"].notna().astype(int)

Where:

1 → The customer left the service.
0 → The customer remains active.


### ⚙️ Preprocessing and Feature Engineering

The processing pipeline includes data cleaning, validation, and feature engineering.

Created features
TenureMonths

Approximate number of months the customer has remained with the company.

NumServices

Number of additional subscribed services:

OnlineSecurity
OnlineBackup
DeviceProtection
TechSupport
StreamingTV
StreamingMovies
HasInternet

Indicates whether the customer has an Internet service.

HasStreaming

Indicates whether the customer uses any streaming services.

SecurityPack

Indicates whether the customer has security or protection-related services.

MonthlyAvgCharge

This feature was also evaluated during the modeling process but was ultimately excluded from the final model.


### 🤖 Evaluated Models

Different Machine Learning algorithms were compared:

Logistic Regression
CatBoost
LightGBM
Random Forest
Decision Tree
Dummy Classifier
Results
Model	Accuracy	Precision	Recall	F1	ROC-AUC
Logistic Regression	74.28%	50.94%	80.94%	62.53%	84.98%
CatBoost	86.26%	70.27%	83.51%	76.32%	93.40%
LightGBM	90.12%	86.17%	74.73%	80.05%	94.14%
Random Forest	82.74%	73.35%	54.82%	62.75%	86.25%
Decision Tree	72.23%	48.68%	86.94%	62.41%	86.18%
Dummy	73.48%	0.00%	0.00%	0.00%	50.00%

LightGBM was selected as the final model based on its overall performance and ROC-AUC.


### 🏆 Final Model — LightGBM

The final model uses LightGBM with the following parameters:

LGBMClassifier(
    colsample_bytree=0.9,
    max_depth=4,
    min_child_samples=50,
    n_estimators=700,
    n_jobs=1,
    objective="binary",
    random_state=12345,
    subsample=0.8,
    verbosity=-1
)

The trained model is serialized using joblib.

```text
models/lightgbm_model.joblib
```

The `.joblib` file is not included in source-code version control. The production model is managed through GitHub Release `v1.0.0` and downloaded during the Docker image build.


### 🔎 Analysis and interpretability

Model interpretability techniques were used to understand which variables have the greatest influence on predictions.

Among them:

Feature Importance.
SHAP.

These tools make it possible to analyze model behavior and relate its predictions to customer characteristics.


### 📊 Previous analysis with Power BI

As part of the initial project stages, exploratory and business analysis was also performed using Power BI.

This analysis made it possible to identify patterns related to:

Churn.
Customer characteristics.
Subscribed services.
Customer behavior.

The Power BI analysis corresponds to an earlier project stage, while the current version focuses on bringing the Machine Learning model into production.


### 🌐 API REST

The application uses FastAPI to expose the model through a REST API.

Principal Endpoint
POST /predict

It receives customer information and returns:

Churn prediction.
Churn probability.

Example input
{
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
Example output
{
  "churn_predicho": 1,
  "probabilidad_churn": 0.9999956167096107
}

Swagger

FastAPI automatically generates an interactive interface for testing the API:

/docs


### 🐳 Docker

The API is containerized with Docker.

The image uses:

FROM python:3.12-slim

It also installs libgomp1, which is required to run LightGBM inside the container.

The model is downloaded during the image build process from the GitHub Release:

v1.0.0

This makes the model available inside the container even though it is not part of the Git repository.

Port

The application uses port:

10000


### ☁️ Render Deployment

The API is currently deployed on Render.

The project architecture is:

Client
   │
   ▼
FastAPI
   │
   ▼
Preprocessing
   │
   ▼
LightGBM
   │
   ▼
Prediction
   │
   ▼
Churn probability

Docker packages:

API.
Processing code.
Prediction code.
Dependencies.
Trained model.

Render subsequently runs the container and exposes the API publicly.


### 🧪 Tests

The project includes tests using pytest.

There are currently 6 automated tests validating API status, valid and invalid inputs, required fields, allowed categories, and the structure and range of the prediction response.

Example:

python -m pytest -v

Current result in CI:

```text
6 passed
```


### 📁 Project Structure

internet_company_churn_prediction/
│
├── data/
│
├── dashboards/
│   └── images/
│
├── models/
│   └── lightgbm_model.joblib
│
├── notebooks/
│
├── src/
│   ├── README.md
│   ├── config.py
│   ├── preprocess.py
│   ├── train.py
│   └── predict.py
│
├── tests/
│   └── test_preprocess.py
│
├── api/
│   └── main.py
│
├── .gitignore
├── README.md
├── README_ES.md
├── requirements.txt
└── requirements-api.txt


### 🛠️ Tecnologies

Python
Pandas
NumPy
Scikit-learn
LightGBM
CatBoost
SHAP
Seaborn
Matplotlib
API
FastAPI
Uvicorn
Pytest
Docker
Render
GitHub Releases
Power BI
Git
GitHub
SSH


### 💼 Business Recommendations

The churn model can be used as a decision-support tool to identify customers at higher risk of leaving.

Some possible actions:

Identify high-risk customers.
Design retention campaigns.
Offer personalized discounts.
Analyze the associated services with the highest churn.
Prioritize customers according to their estimated probability of leaving.

The model does not replace business decisions; it provides information to support retention strategies.


### 🔮 Future Improvements

Some possible improvements for future versions:

- Implement model monitoring.
- Log production metrics.
- Monitor data drift and prediction drift.
- Create a frontend interface to consume API.
- Implement batch predictions using CSV files.
- Automate model training and retraining with new historical data.
- Implement authentication and authorization for API.
- Implement a more comprehensive system for versioning and managing model artifacts.
- Incorporate integration tests and load tests.
- Explore new techniques for optimization, feature selection, and model interpretation.
- Evaluate different classification thresholds based on business costs.


### ✅ Current Project Status

The project currently has a complete Machine Learning workflow through production:

Raw Data
  ↓
Preprocessing
  ↓
Feature Engineering
  ↓
Training
  ↓
Evaluation
  ↓
LightGBM selection
  ↓
Optimization
  ↓
Model saving
  ↓
FastAPI
  ↓
Docker
  ↓
Render
  ↓
API in produciton

Status

🟢 Model entrenado

🟢 Model guardado

🟢 Pipeline modular

🟢 API REST

🟢 Docker

🟢 GitHub Release

🟢 Deployed on Render

🟢 Predictions verified in production


### 👨‍💻 Author

Angel Enriquez

Data Scientist | Mechatronics Engineer

This project is part of my Data Science portfolio and demonstrates a complete workflow from data processing and Machine Learning to deploying a model in production.
