# app/services/train_service.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

def train_classifier():
    # Example dataset: binary classification
    data = pd.DataFrame({
        "feature1": [0.1, 0.2, 0.8, 0.9],
        "feature2": [1.1, 1.3, 3.2, 3.5],
        "label": [0, 0, 1, 1]
    })

    X = data[["feature1", "feature2"]]
    y = data["label"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Save model
    joblib.dump(model, "app/models/classifier.pkl")

    return {"message": "Model trained and saved successfully"}