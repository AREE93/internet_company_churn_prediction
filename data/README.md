# Data

This directory contains the data structure used for the Interconnect Customer Churn Prediction project.

## Raw Data

The `raw/` directory is intended to store the original datasets provided for the project.

The original data is not included in this repository.

## Processed Data

The `processed/` directory is intended to store datasets generated during preprocessing and feature engineering.

Examples of transformations include:

- Data cleaning
- Date conversion
- Creation of the target variable `Churn`
- Creation of `TenureMonths`
- Feature engineering
- Data preparation for model training

Processed datasets are not included in the repository to keep the repository lightweight and avoid redistributing the original data.

## Data Source

The project uses customer information from Interconnect, including:

- Customer demographics
- Contract information
- Internet services
- Phone services
- Monthly charges
- Total charges
- Customer tenure

The data used for this project was originally provided as part of a Data Science training project.
