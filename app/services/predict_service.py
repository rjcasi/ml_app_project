import joblib

# Load pre-trained model
model = joblib.load("models/classifier.pkl")

def predict(data: dict):
    # Example: expects {"features": [0.5, 1.2, 3.4]}
    features = data["features"]
    return model.predict([features]).tolist()