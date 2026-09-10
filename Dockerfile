FROM python:3.12-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libgomp1 \
        curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements-api.txt .

RUN pip install --no-cache-dir -r requirements-api.txt

COPY api/ ./api/
COPY src/ ./src/

RUN mkdir -p models

RUN curl -L \
    -o models/lightgbm_model.joblib \
    https://github.com/AREE93/internet_company_churn_prediction/releases/download/v1.0.0/lightgbm_model.joblib

EXPOSE 10000

CMD ["python", "-m", "fastapi", "run", "api/main.py", "--host", "0.0.0.0", "--port", "10000"]
