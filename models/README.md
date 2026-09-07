# Models

This directory is intended to store trained Machine Learning models generated during the project.

## Final Model

The final selected model is a LightGBM classifier trained to predict customer churn.

LightGBM was selected after comparing several classification algorithms and performing hyperparameter tuning.

## Models Evaluated

The following models were evaluated:

- Dummy Classifier
- Logistic Regression
- Decision Tree
- Random Forest
- CatBoost
- LightGBM

## Model Selection

LightGBM achieved the best overall performance after hyperparameter optimization, while CatBoost obtained the second-best overall performance.

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

## Final Model Performance

The final model achieved approximately:

- Accuracy: 92.96%
- Precision: 89.24%
- Recall: 83.51%
- F1 Score: 86.28%
- ROC-AUC: 96.62%

These metrics correspond to the evaluation performed on the test dataset.

## Model Serialization

The trained model can be serialized using formats such as:

- Pickle (`.pkl`)
- Joblib (`.joblib`)

Model files are excluded from version control by the project's `.gitignore` configuration.

## Future Deployment

The model directory can later be integrated into a production workflow involving:

- FastAPI
- Docker
- Cloud deployment
- Model monitoring
- Automated retraining
