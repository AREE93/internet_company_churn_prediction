🇲🇽 Español | 🇺🇸 [English](README.md)


Predicción de Churn de Clientes — Internet Company


Proyecto de Machine Learning para predecir la cancelación de clientes (churn) de una empresa de telecomunicaciones. El proyecto cubre el flujo completo, desde el análisis y procesamiento de datos hasta el entrenamiento, evaluación, interpretación y despliegue de un modelo de Machine Learning mediante una API REST.

🚀 API en producción

API desplegada en Render:

https://internet-company-churn-prediction.onrender.com

Swagger UI:

https://internet-company-churn-prediction.onrender.com/docs

La API permite enviar información de un cliente y obtener una predicción de churn junto con su probabilidad.

Ejemplo de respuesta
{
  "churn_predicho": 1,
  "probabilidad_churn": 0.9999956167096107
}
📌 Descripción del proyecto

El objetivo principal es desarrollar un modelo capaz de identificar clientes con riesgo de abandonar el servicio.

El proyecto sigue un flujo completo de Data Science y Machine Learning:

Carga y preparación de los datos.
Limpieza y validación.
Ingeniería de características.
Definición de la variable objetivo.
Comparación de diferentes modelos.
Evaluación mediante múltiples métricas.
Selección y optimización del modelo final.
Interpretación del modelo.
Guardado del modelo entrenado.
Desarrollo de una API REST con FastAPI.
Containerización mediante Docker.
Despliegue en Render.
📊 Dataset

El proyecto utiliza datos de clientes de una empresa de telecomunicaciones.

Entre las variables originales se encuentran:

Información demográfica.
Servicios contratados.
Tipo de contrato.
Método de pago.
Facturación electrónica.
Cargos mensuales.
Cargos totales.
Fecha de inicio.
Fecha de finalización.
Variable objetivo

La variable Churn se construye a partir de EndDate:

df["Churn"] = df["EndDate"].notna().astype(int)

Donde:

1 → El cliente abandonó el servicio.
0 → El cliente continúa activo.
⚙️ Preprocesamiento e ingeniería de características

El pipeline de procesamiento incluye limpieza, validación e ingeniería de características.

Características creadas
TenureMonths

Número aproximado de meses que el cliente ha permanecido en la empresa.

NumServices

Número de servicios adicionales contratados:

OnlineSecurity
OnlineBackup
DeviceProtection
TechSupport
StreamingTV
StreamingMovies
HasInternet

Indica si el cliente tiene contratado un servicio de Internet.

HasStreaming

Indica si el cliente utiliza alguno de los servicios de streaming.

SecurityPack

Indica si el cliente cuenta con servicios relacionados con seguridad o protección.

MonthlyAvgCharge

Esta característica también fue evaluada durante el proceso de modelado, pero finalmente fue descartada del modelo final.

🤖 Modelos evaluados

Se compararon diferentes algoritmos de Machine Learning:

Logistic Regression
CatBoost
LightGBM
Random Forest
Decision Tree
Dummy Classifier
Resultados
Modelo	Accuracy	Precision	Recall	F1	ROC-AUC
Logistic Regression	74.28%	50.94%	80.94%	62.53%	84.98%
CatBoost	86.26%	70.27%	83.51%	76.32%	93.40%
LightGBM	90.12%	86.17%	74.73%	80.05%	94.14%
Random Forest	82.74%	73.35%	54.82%	62.75%	86.25%
Decision Tree	72.23%	48.68%	86.94%	62.41%	86.18%
Dummy	73.48%	0.00%	0.00%	0.00%	50.00%

LightGBM fue seleccionado como modelo final debido a su combinación de desempeño general y ROC-AUC.

🏆 Modelo final — LightGBM

El modelo final utiliza LightGBM con los siguientes parámetros:

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

El modelo entrenado se guarda localmente mediante joblib:

models/lightgbm_model.joblib

El archivo del modelo no se incluye directamente en el repositorio debido a su tamaño y está gestionado mediante un GitHub Release.

🔎 Análisis e interpretabilidad

Durante el análisis del modelo se utilizaron técnicas de interpretación para comprender qué variables tienen mayor influencia sobre las predicciones.

Entre ellas:

Feature Importance.
SHAP.

Estas herramientas permiten analizar el comportamiento del modelo y relacionar sus predicciones con las características de los clientes.

📊 Análisis anterior con Power BI

Como parte de las etapas iniciales del proyecto también se realizó un análisis exploratorio y de negocio mediante Power BI.

Este análisis permitió identificar patrones relacionados con:

Churn.
Características de los clientes.
Servicios contratados.
Comportamiento de los clientes.

El análisis de Power BI corresponde a una etapa previa del proyecto, mientras que la versión actual se enfoca en llevar el modelo de Machine Learning a una etapa de producción.

🌐 API REST

La aplicación utiliza FastAPI para exponer el modelo mediante una API REST.

Endpoint principal
POST /predict

Recibe la información de un cliente y devuelve:

Predicción de churn.
Probabilidad de churn.
Ejemplo de entrada
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
Ejemplo de salida
{
  "churn_predicho": 1,
  "probabilidad_churn": 0.9999956167096107
}
Swagger

FastAPI genera automáticamente una interfaz interactiva para probar la API:

/docs
🐳 Docker

La API está containerizada mediante Docker.

La imagen utiliza:

FROM python:3.12-slim

Además, instala libgomp1, necesario para ejecutar LightGBM dentro del contenedor.

El modelo se descarga durante el proceso de construcción de la imagen desde el GitHub Release:

v1.0.0

Esto permite que el modelo esté disponible dentro del contenedor incluso cuando no forma parte del repositorio Git.

Puerto

La aplicación utiliza el puerto:

10000
☁️ Despliegue en Render

La API está desplegada actualmente en Render.

La arquitectura del proyecto es:

Cliente
   │
   ▼
FastAPI
   │
   ▼
Preprocesamiento
   │
   ▼
LightGBM
   │
   ▼
Predicción
   │
   ▼
Probabilidad de churn

Docker se encarga de empaquetar:

API.
Código de procesamiento.
Código de predicción.
Dependencias.
Modelo entrenado.

Render ejecuta posteriormente el contenedor y expone la API públicamente.

🧪 Tests

El proyecto incluye pruebas utilizando pytest.

Actualmente se validan principalmente funciones relacionadas con el procesamiento y validación de datos.

Ejemplo:

python -m pytest -v

Resultado actual:

2 passed
📁 Estructura del proyecto
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
🛠️ Tecnologías
Lenguaje
Python
Data Science
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
Testing
Pytest
Deployment
Docker
Render
GitHub Releases
Visualización
Power BI
Control de versiones
Git
GitHub
SSH
💼 Recomendaciones de negocio

El modelo de churn puede utilizarse como una herramienta de apoyo para identificar clientes con mayor riesgo de abandono.

Algunas posibles acciones son:

Identificar clientes de alto riesgo.
Diseñar campañas de retención.
Ofrecer incentivos personalizados.
Analizar los servicios asociados con mayor churn.
Priorizar clientes según su probabilidad estimada de abandono.

El modelo no sustituye las decisiones de negocio; proporciona información para apoyar estrategias de retención.

🔮 Mejoras futuras

Algunas posibles mejoras para futuras versiones:

Implementar monitoreo del modelo.
Crear una interfaz frontend para consumir la API.
Agregar pruebas automatizadas para el endpoint /predict.
Implementar validación más estricta del esquema de entrada mediante Pydantic.
Automatizar el entrenamiento del modelo.
Implementar CI/CD.
Registrar métricas de producción.
Implementar model versioning.
Incorporar nuevas técnicas de optimización e interpretación.
✅ Estado actual del proyecto

El proyecto cuenta actualmente con un flujo completo de Machine Learning hasta producción:

Datos
  ↓
Preprocesamiento
  ↓
Feature Engineering
  ↓
Entrenamiento
  ↓
Evaluación
  ↓
Selección de LightGBM
  ↓
Optimización
  ↓
Guardado del modelo
  ↓
FastAPI
  ↓
Docker
  ↓
Render
  ↓
API en producción
Estado

🟢 Modelo entrenado

🟢 Modelo guardado

🟢 Pipeline modular

🟢 API REST

🟢 Docker

🟢 GitHub Release

🟢 Despliegue en Render

🟢 Predicciones verificadas en producción

👨‍💻 Autor

Angel Enriquez

Data Scientist | Mechatronics Engineer

Este proyecto forma parte de mi portafolio de Data Science y demuestra un flujo completo desde el procesamiento de datos y Machine Learning hasta el despliegue de un modelo en producción.