import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score, roc_auc_score)

from lightgbm import LGBMClassifier

from src.preprocess import (
    preprocess_data,
    create_target,
    prepare_features
)

import joblib
from pathlib import Path

def train_model(df):
    """
    Preprocesa los datos, divide el dataset,
    entrena un modelo LightGBM y evalúa su rendimiento.
    """

    # ==========================
    # PREPROCESAMIENTO
    # ==========================

    df_processed = preprocess_data(df)

    # Crear variable objetivo
    df_processed = create_target(df_processed)

    #Separar features y target
    X, y = prepare_features(
        df_processed)

    # ==========================
    # TRAIN / TEST SPLIT
    # ==========================

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        stratify=y,
        random_state=12345
    )

    # ==========================
    # COLUMNAS CATEGÓRICAS
    # ==========================

    categorical_features = X_train.select_dtypes(
        include="object"
    ).columns.tolist()

    for column in categorical_features:
        X_train[column] = X_train[column].astype("category")
        X_test[column] = X_test[column].astype("category")

    # ==========================
    # MODELO
    # ==========================

    model = LGBMClassifier(
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

    model.fit(
        X_train,
        y_train
    )

    # ==========================
    # GUARDADO DE MODELO
    # ==========================

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

    # ==========================
    # PREDICCIONES
    # ==========================

    predictions = model.predict(X_test)

    probabilities = model.predict_proba(
        X_test
    )[:, 1]

    # ==========================
    # MÉTRICAS
    # ==========================

    metrics = {
        "accuracy": accuracy_score(
            y_test,
            predictions
        ),
        "precision": precision_score(
            y_test,
            predictions
        ),
        "recall": recall_score(
            y_test,
            predictions
        ),
        "f1": f1_score(
            y_test,
            predictions
        ),
        "roc_auc": roc_auc_score(
            y_test,
            probabilities
        )
    }

    return model, metrics
