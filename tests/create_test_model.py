import joblib
import pandas as pd

from pathlib import Path
from lightgbm import LGBMClassifier

from src.config import LGBM_PARAMS
from src.preprocess import preprocess_data, prepare_features


def create_test_data():
    """
    Crea datos sintéticos para generar un modelo
    utilizado únicamente durante las pruebas.
    """

    data = []

    for i in range(20):
        data.append({
            "customerID": f"TEST{i:03d}",
            "gender": "Female" if i % 2 == 0 else "Male",
            "SeniorCitizen": i % 2,
            "Partner": "Yes" if i % 2 == 0 else "No",
            "Dependents": "No" if i % 3 == 0 else "Yes",
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
            "MonthlyCharges": 70.5 + i,
            "TotalCharges": str(846.0 + (i * 50)),
            "EndDate": (
                "2020-01-01"
                if i % 2 == 0
                else None
            )
        })

    return pd.DataFrame(data)


def main():

    df = create_test_data()

    # Utilizamos exactamente el mismo
    # preprocesamiento del proyecto.
    df_processed = preprocess_data(df)

    # Crear variable objetivo.
    df_processed["Churn"] = (
        df_processed["EndDate"]
        .notna()
        .astype(int)
    )

    # Separar features y target.
    X, y = prepare_features(df_processed)

    # Convertir variables categóricas.
    categorical_features = X.select_dtypes(
        include="object"
    ).columns.tolist()

    for column in categorical_features:
        X[column] = X[column].astype("category")

    # Crear modelo utilizando la misma configuración
    # que el modelo real.
    model = LGBMClassifier(
        **LGBM_PARAMS
    )

    model.fit(
        X,
        y
    )

    # Ruta del proyecto.
    project_root = Path(__file__).resolve().parent.parent

    model_path = (
        project_root
        / "models"
        / "lightgbm_model.joblib"
    )

    joblib.dump(
        model,
        model_path
    )

    print(
        f"Modelo de prueba creado en: {model_path}"
    )


if __name__ == "__main__":
    main()