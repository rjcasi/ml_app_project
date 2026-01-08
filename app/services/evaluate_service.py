# app/services/evaluate_service.py
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

def evaluate_classifier():
    # Example dataset (same as training)
    data = pd.DataFrame({
        "feature1": [0.1, 0.2, 0.8, 0.9],
        "feature2": [1.1, 1.3, 3.2, 3.5],
        "label": [0, 0, 1, 1]
    })

    X = data[["feature1", "feature2"]]
    y = data["label"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

    # Load trained model
    model = joblib.load("app/models/classifier.pkl")

    # Predictions
    y_pred = model.predict(X_test)

    # Metrics
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred).tolist()
    report = classification_report(y_test, y_pred, output_dict=True)

    return {
        "accuracy": acc,
        "confusion_matrix": cm,
        "classification_report": report
    }