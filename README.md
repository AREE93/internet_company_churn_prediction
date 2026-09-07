# Interconnect Customer Churn Prediction & Retention Analytics

## 📌 Descripción del proyecto

Este proyecto desarrolla una solución de Machine Learning para predecir la probabilidad de cancelación de clientes (churn) de una empresa de telecomunicaciones.

El objetivo es identificar clientes con mayor riesgo de abandonar el servicio y proporcionar información que permita diseñar estrategias de retención más efectivas.

El proyecto combina análisis exploratorio de datos, ingeniería de características, entrenamiento y comparación de modelos de Machine Learning, interpretabilidad y visualización de resultados mediante Power BI.

---

## 🎯 Objetivo de negocio

Desarrollar un modelo predictivo capaz de identificar clientes con riesgo de churn y proporcionar información útil para que el área de retención pueda:

- Identificar clientes de alto riesgo.
- Priorizar acciones de retención.
- Diseñar campañas segmentadas.
- Detectar patrones asociados con la cancelación.
- Medir y monitorear el riesgo de churn.

---

## 📊 Dataset

El conjunto de datos contiene información relacionada con los clientes, sus servicios contratados, características demográficas, cargos y duración de la relación con la empresa.

Entre las principales variables se encuentran:

- `InternetService`
- `OnlineSecurity`
- `OnlineBackup`
- `DeviceProtection`
- `TechSupport`
- `StreamingTV`
- `StreamingMovies`
- `Type`
- `PaperlessBilling`
- `PaymentMethod`
- `MonthlyCharges`
- `TotalCharges`
- `gender`
- `SeniorCitizen`
- `Partner`
- `Dependents`
- `MultipleLines`

La variable objetivo `Churn` se construyó a partir de la existencia de una fecha de cancelación (`EndDate`).

---

## 🔧 Preprocesamiento e ingeniería de características

Se realizaron diferentes transformaciones para preparar los datos para el modelado:

- Conversión y limpieza de fechas.
- Conversión de `TotalCharges` a formato numérico.
- Creación de la variable objetivo `Churn`.
- Cálculo de la antigüedad del cliente mediante `TenureMonths`.
- Codificación de variables categóricas.
- Tratamiento de valores faltantes.
- Escalado de variables cuando fue necesario.
- División de los datos en conjuntos de entrenamiento y prueba.

También se generaron características adicionales:

- `NumServices`
- `HasInternet`
- `HasStreaming`
- `SecurityPack`
- `MonthlyAvgCharge`

Posteriormente se evaluó el aporte de las características derivadas y se realizaron ajustes al conjunto final de variables utilizado por los modelos.

---

## 🤖 Modelos evaluados

Se compararon diferentes algoritmos de clasificación:

- Dummy Classifier
- Logistic Regression
- Decision Tree
- Random Forest
- CatBoost
- LightGBM

El `Dummy Classifier` se utilizó como modelo baseline para establecer una referencia de rendimiento.

---

## 📈 Evaluación de modelos

Los modelos fueron evaluados utilizando:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

Resultados obtenidos:

| Modelo | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 92.62% | 83.63% | 89.72% | 86.57% | 97.70% |
| CatBoost | 92.62% | 85.47% | 86.94% | 86.20% | 97.05% |
| LightGBM | 92.96% | 89.24% | 83.51% | 86.28% | 96.62% |
| Random Forest | 89.10% | 87.88% | 68.31% | 76.87% | 93.17% |
| Decision Tree | 74.39% | 50.97% | 89.72% | 65.01% | 88.36% |
| Dummy | 73.48% | 0.00% | 0.00% | 0.00% | 50.00% |

---

## 🏆 Modelo seleccionado

Después de comparar los modelos y realizar ajustes de hiperparámetros, **LightGBM fue seleccionado como modelo final** debido a su equilibrio entre rendimiento predictivo y precisión en la identificación de clientes.

El modelo alcanzó:

- **Accuracy:** 92.96%
- **Precision:** 89.24%
- **Recall:** 83.51%
- **F1:** 86.28%
- **ROC-AUC:** 96.62%

CatBoost obtuvo el segundo mejor desempeño general.

La selección del modelo no se realizó únicamente considerando Accuracy, sino analizando diferentes métricas y el objetivo de negocio relacionado con la identificación de clientes en riesgo.

---

## 🔎 Interpretabilidad

Se utilizó Feature Importance para identificar las variables con mayor influencia en el modelo.

Las variables con mayor importancia fueron:

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

También se incorporó análisis mediante **SHAP** para profundizar en la interpretación de las predicciones y analizar cómo determinadas características influyen en el riesgo de churn.

---

## 📊 Dashboard

Los resultados del modelo fueron integrados en un dashboard desarrollado en **Power BI**.

El dashboard permite visualizar:

- Rendimiento del modelo.
- Distribución de clientes según riesgo.
- Probabilidad de churn.
- Clientes con mayor riesgo.
- Importancia de las variables.
- Información útil para estrategias de retención.

---

## 💼 Recomendaciones de negocio

A partir de los resultados obtenidos se proponen las siguientes acciones:

1. Priorizar clientes con mayor probabilidad de churn.
2. Implementar campañas de retención segmentadas.
3. Prestar especial atención a clientes con poca antigüedad.
4. Analizar clientes con cargos mensuales elevados.
5. Incentivar contratos de mayor duración mediante ofertas personalizadas.
6. Utilizar las predicciones para crear sistemas de alerta de riesgo.
7. Medir el impacto de las campañas de retención.
8. Reentrenar periódicamente el modelo con nuevos datos.

---

## 🛠️ Tecnologías utilizadas

- Python
- Pandas
- NumPy
- Scikit-learn
- LightGBM
- CatBoost
- Matplotlib
- Seaborn
- SHAP
- Jupyter Notebook
- Power BI
- Git
- GitHub

---

## 📁 Estructura del proyecto

```text
interconnect-churn-prediction/
│
├── data/
├── notebooks/
├── dashboard/
├── models/
├── src/
│
├── .gitignore
├── README.md
└── requirements.txt

