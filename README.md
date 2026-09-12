🇺🇸 English | 🇲🇽 [Español](README_ES.md)

# Interconnect Customer Churn Prediction & Retention Analytics

Machine Learning project for predicting customer churn in a telecommunications company and supporting data-driven customer retention strategies.

The project covers the complete workflow, from data preprocessing and feature engineering to model training, evaluation, interpretability, API deployment, and containerization.

## 🚀 Live API

The prediction API is deployed and available through Render:

**API:** https://internet-company-churn-prediction.onrender.com

**Swagger documentation:** https://internet-company-churn-prediction.onrender.com/docs

The API receives customer information and returns:

* Churn prediction
* Churn probability

Example response:

```json
{
  "churn_predicho": 1,
  "probabilidad_churn": 0.9999956167096107
}
```

---

## 📌 Project Overview

Customer churn is an important business problem for telecommunications companies because retaining existing customers can be more efficient than acquiring new ones.

This project develops a Machine Learning solution capable of identifying customers with a higher probability of cancelling their service.

The solution combines:

* Exploratory Data Analysis
* Data cleaning
* Feature engineering
* Machine Learning model comparison
* Model optimization
* Model interpretability
* Power BI visualization
* REST API development
* Docker containerization
* Cloud deployment

The final objective is not only to predict churn, but also to provide information that can support customer retention decisions.

---

## 🎯 Business Objective

Develop a predictive solution capable of identifying customers at risk of churn so that the retention team can:

* Identify high-risk customers.
* Prioritize retention actions.
* Design targeted campaigns.
* Detect patterns associated with customer cancellation.
* Monitor churn risk.
* Measure the impact of retention strategies.

---

## 📊 Dataset

The dataset contains information about customers, their contracted services, demographic characteristics, charges, and relationship duration with the company.

Relevant variables include:

* `InternetService`
* `OnlineSecurity`
* `OnlineBackup`
* `DeviceProtection`
* `TechSupport`
* `StreamingTV`
* `StreamingMovies`
* `Type`
* `PaperlessBilling`
* `PaymentMethod`
* `MonthlyCharges`
* `TotalCharges`
* `gender`
* `SeniorCitizen`
* `Partner`
* `Dependents`
* `MultipleLines`
* `BeginDate`
* `EndDate`

The target variable `Churn` was created from the existence of a customer cancellation date:

```python
df["Churn"] = df["EndDate"].notna().astype(int)
```

---

## 🔧 Data Preprocessing & Feature Engineering

The preprocessing pipeline was designed to be reusable for both model training and new customer predictions.

The main transformations include:

* Date conversion and cleaning.
* Conversion of `TotalCharges` to numeric format.
* Missing-value treatment.
* Target creation.
* Customer tenure calculation.
* Categorical feature preparation.
* Train/test splitting.

### Engineered Features

Additional features were created to capture customer behavior and service characteristics:

* `TenureMonths`
* `NumServices`
* `HasInternet`
* `HasStreaming`
* `SecurityPack`

`MonthlyAvgCharge` was also evaluated during feature experimentation but was not included in the final model.

The final preprocessing pipeline is implemented in:

```text
src/preprocess.py
```

---

## 🤖 Models Evaluated

Several classification algorithms were compared:

* Dummy Classifier
* Logistic Regression
* Decision Tree
* Random Forest
* CatBoost
* LightGBM

The `Dummy Classifier` was used as a baseline to establish a reference level of performance.

---

## 📈 Model Evaluation

The models were evaluated using multiple classification metrics:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC

The comparison was not based exclusively on Accuracy. Precision, Recall, F1 Score, and ROC-AUC were also considered in the context of the business objective.

### Model Comparison

| Model               | Accuracy | Precision | Recall |     F1 | ROC-AUC |
| ------------------- | -------: | --------: | -----: | -----: | ------: |
| Logistic Regression |   74.28% |    50.94% | 80.94% | 62.53% |  84.98% |
| CatBoost            |   86.26% |    70.27% | 83.51% | 76.32% |  93.40% |
| LightGBM            |   90.12% |    86.17% | 74.73% | 80.05% |  94.14% |
| Random Forest       |   82.74% |    73.35% | 54.82% | 62.75% |  86.25% |
| Decision Tree       |   72.23% |    48.68% | 86.94% | 62.41% |  86.18% |
| Dummy               |   73.48% |     0.00% |  0.00% |  0.00% |  50.00% |


> **Note:** The table above documents the model-comparison results from the project evaluation. The final LightGBM pipeline was subsequently refined through feature and hyperparameter adjustments.

---

## 🏆 Final Model

After model comparison and subsequent tuning, **LightGBM was selected as the final model**.

The final model uses the following configuration:

```python
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
```

The model is serialized locally using `joblib`:

```text
models/lightgbm_model.joblib
```

The model artifact is intentionally excluded from Git version control because of its size and is distributed through the project's GitHub Release.

---

## 🔎 Model Interpretability

Model interpretability was incorporated to understand which variables contribute most to the predictions.

Feature Importance was used to identify relevant variables, including:

1. `TotalCharges`
2. `TenureMonths`
3. `MonthlyCharges`
4. `Type`
5. `gender`
6. `InternetService`
7. `OnlineBackup`
8. `PaperlessBilling`
9. `NumServices`
10. `PaymentMethod`

SHAP analysis was also incorporated to provide a deeper interpretation of model predictions and understand how individual characteristics influence churn risk.

---

## 📊 Power BI Dashboard

The project includes a Power BI dashboard designed to communicate the model results from a business perspective.

The dashboard allows analysis of:

* Model performance.
* Customer risk distribution.
* Churn probability.
* Customers with higher predicted risk.
* Feature importance.
* Information relevant to retention strategies.

---

## 🌐 REST API

The trained model is exposed through a REST API developed with **FastAPI**.

### Available endpoints

#### `GET /`

Returns the API status.

Example:

```json
{
  "message": "Internet Company Churn Prediction API",
  "status": "running"
}
```

#### `POST /predict`

Receives customer information and returns the predicted churn class and probability.

Example request:

```json
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
```

Example response:

```json
{
  "churn_predicho": 1,
  "probabilidad_churn": 0.9999956167096107
}
```

Interactive API documentation is available through Swagger:

`/docs`

---

## 🐳 Docker

The API was containerized using Docker.

The Docker image includes:

* Python 3.12
* FastAPI
* LightGBM
* Required API dependencies
* The trained model artifact
* System dependencies required by LightGBM

The model is downloaded during the Docker build from the project's GitHub Release.

### Build the image

```bash
docker build -t churn-api .
```

### Run the container

```bash
docker run --rm -p 10000:10000 churn-api
```

The API will then be available at:

```text
http://localhost:10000
```

Swagger:

```text
http://localhost:10000/docs
```

---

## ☁️ Deployment

The application is deployed using **Render**.

Deployment architecture:

```text
Customer
   │
   ▼
FastAPI
   │
   ▼
Prediction Pipeline
   │
   ├── Data validation
   ├── Data cleaning
   ├── Feature engineering
   └── Feature preparation
   │
   ▼
LightGBM Model
   │
   ▼
Churn Prediction
   │
   └── Churn probability
```

The deployed service is available at:

```text
https://internet-company-churn-prediction.onrender.com
```

---

## 🧪 Testing

The project includes automated tests for preprocessing validation using `pytest`.

Current tests verify:

* Successful validation when required columns are present.
* Detection of missing required columns.

Run the tests with:

```bash
python -m pytest -v
```

---

## 📁 Project Structure

```text
internet_company_churn_prediction/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── dashboards/
│   └── images/
│
├── models/
│   ├── README.md
│   └── .gitkeep
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
├── api/
│   └── main.py
│
├── tests/
│   └── test_preprocess.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── requirements-api.txt
```

---

## 🛠️ Technologies

### Data Science

* Python
* Pandas
* NumPy
* Scikit-learn
* LightGBM
* CatBoost
* Matplotlib
* Seaborn
* SHAP
* Jupyter Notebook

### Data Visualization

* Power BI

### Deployment & Engineering

* FastAPI
* Docker
* Git
* GitHub
* Render
* Joblib
* Pytest

---

## 💼 Business Recommendations

Based on the analysis and model predictions, potential retention actions include:

1. Prioritize customers with high predicted churn probability.
2. Implement segmented retention campaigns.
3. Pay particular attention to customers with lower tenure.
4. Analyze customers with higher monthly charges.
5. Encourage longer-term contracts through personalized offers.
6. Implement risk alerts based on model predictions.
7. Measure the impact of retention campaigns.
8. Periodically retrain the model using new customer data.

---

## 🔮 Future Improvements

Potential next steps for the project include:

* Expand automated testing.
* Add CI/CD with GitHub Actions.
* Improve API input validation with Pydantic models.
* Add model monitoring.
* Monitor prediction drift and data drift.
* Implement automated model retraining.
* Add authentication to the API.
* Improve the Power BI dashboard.
* Add more detailed SHAP analysis.
* Evaluate different classification thresholds according to business costs.

---

## 👤 Project Status

The project currently includes an end-to-end Machine Learning pipeline:

```text
Data
 ↓
Preprocessing
 ↓
Feature Engineering
 ↓
Model Training
 ↓
Model Evaluation
 ↓
LightGBM
 ↓
Joblib
 ↓
FastAPI
 ↓
Docker
 ↓
Render
 ↓
Production API
```

The prediction service has been successfully tested locally and in the deployed environment.


👨‍💻 Autor

Angel Enriquez

Data Scientist | Mechatronics Engineer

This project is part of my Data Science portfolio and demonstrates an end-to-end workflow, from data preprocessing and Machine Learning to production model deployment.
