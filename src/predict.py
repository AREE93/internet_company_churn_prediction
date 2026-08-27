from pathlib import Path
import joblib
import pandas as pd


from src.preprocess import (
    preprocess_data,
    prepare_prediction_data
)


def load_model():
    """
    Carga el modelo LightGBM entrenado.
    """

    project_root = Path(__file__).resolve().parent.parent

    model_path = (
        project_root
        / "models"
        / "lightgbm_model.joblib"
    )

    model = joblib.load(model_path)

    return model


def predict_churn(df):
    """
    Genera predicciones de churn para nuevos clientes.

    Parameters
    ----------
    df : pandas.DataFrame
        Datos de nuevos clientes.

    Returns
    -------
    pandas.DataFrame
        DataFrame con predicción y probabilidad de churn.
    """

    # ==========================
    # CARGAR MODELO
    # ==========================

    model = load_model()

    # ==========================
    # PREPROCESAMIENTO
    # ==========================

    df_processed = preprocess_data(df)

    X = prepare_prediction_data(
        df_processed
    )

    # ==========================
    # COLUMNAS CATEGÓRICAS
    # ==========================

    categorical_features = X.select_dtypes(
        include="object"
    ).columns.tolist()

    for column in categorical_features:
        X[column] = X[column].astype(
            "category"
        )

    # ==========================
    # PREDICCIONES
    # ==========================

    predictions = model.predict(X)

    probabilities = model.predict_proba(X)[:, 1]

    # ==========================
    # RESULTADOS
    # ==========================

    results = df.copy()

    results["Churn_predicho"] = predictions

    results["Probabilidad_churn"] = probabilities

    return results
