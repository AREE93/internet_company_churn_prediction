import pandas as pd
import pytest

from src.preprocess import validate_columns


def test_validate_columns_success():
    df = pd.DataFrame({
        "BeginDate": ["2020-01-01"],
        "TotalCharges": ["100"]
    })

    required_columns = [
        "BeginDate",
        "TotalCharges"
    ]

    validate_columns(
        df,
        required_columns
    )


def test_validate_columns_missing_column():
    df = pd.DataFrame({
        "BeginDate": ["2020-01-01"]
    })

    required_columns = [
        "BeginDate",
        "TotalCharges"
    ]

    with pytest.raises(ValueError):
        validate_columns(
            df,
            required_columns
        )