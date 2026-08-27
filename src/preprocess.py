import pandas as pd


def clean_data(df):
    """
    Realiza la limpieza básica del DataFrame.

    La función puede utilizarse tanto con datos históricos
    como con nuevos datos para predicción.
    """

    df = df.copy()

    # ==========================
    # TOTAL CHARGES
    # ==========================

    if "TotalCharges" in df.columns:

        df["TotalCharges"] = pd.to_numeric(
            df["TotalCharges"],
            errors="coerce"
        )

        df["TotalCharges"] = (
            df["TotalCharges"]
            .fillna(0)
        )

    # ==========================
    # BEGIN DATE
    # ==========================

    if "BeginDate" in df.columns:

        df["BeginDate"] = pd.to_datetime(
            df["BeginDate"],
            errors="coerce"
        )

    # ==========================
    # END DATE
    # ==========================

    if "EndDate" in df.columns:

        df["EndDate"] = pd.to_datetime(
            df["EndDate"],
            errors="coerce"
        )

    return df


def create_features(df, fecha_corte="2020-02-01"):
    """
    Crea la variable objetivo y las características
    utilizadas en el modelo.
    """

    df = df.copy()

    # Verificar columna necesaria
    if "BeginDate" not in df.columns:
        raise ValueError(
            "La columna 'BeginDate' es necesaria "
            "para calcular TenureMonths."
        )

    # Fecha de referencia
    fecha_corte = pd.Timestamp(fecha_corte)

    # Antigüedad del cliente en meses
    df["TenureMonths"] = (
        (fecha_corte - df["BeginDate"]).dt.days / 30.44
    ).round(0).astype(int)

    # Servicios adicionales
    servicios = [
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies"
    ]

    # Número de servicios contratados
    df["NumServices"] = (
        df[servicios] == "Yes"
    ).sum(axis=1)

    # Cliente con internet
    df["HasInternet"] = (
        df["InternetService"] != "No"
    ).astype(int)

    # Cliente con algún servicio de streaming
    df["HasStreaming"] = (
        (df["StreamingTV"] == "Yes")
        | (df["StreamingMovies"] == "Yes")
    ).astype(int)

    # Cliente con seguridad o protección
    df["SecurityPack"] = (
        (df["OnlineSecurity"] == "Yes")
        | (df["DeviceProtection"] == "Yes")
    ).astype(int)

    return df


def create_target(df):
    """
    Crea la variable objetivo Churn.

    Un cliente se considera churn cuando tiene
    una fecha registrada en EndDate.
    """

    df = df.copy()

    df["Churn"] = (
        df["EndDate"]
        .notna()
        .astype(int)
    )

    return df


def prepare_features(df):
    """
    Separa las variables predictoras de la variable objetivo.

    Returns
    -------
    X : pandas.DataFrame
        Variables utilizadas para el entrenamiento.

    y : pandas.Series
        Variable objetivo.
    """

    X = df.drop(
        columns=[
            "customerID",
            "BeginDate",
            "EndDate",
            "Churn"
        ]
    )

    y = df["Churn"]

    return X, y


def prepare_prediction_data(df):
    """
    Prepara nuevos datos para realizar predicciones.

    Elimina columnas que no son utilizadas por el modelo.
    """

    X = df.drop(
        columns=[
            "customerID",
            "BeginDate",
            "EndDate",
            "Churn"
        ],
        errors="ignore"
    )

    return X


def preprocess_data(df, fecha_corte="2020-02-01"):
    """
    Ejecuta todo el flujo de limpieza e ingeniería
    de características.
    """

    df = clean_data(df)

    df = create_features(
        df,
        fecha_corte
    )

    return df