from fastapi import APIRouter
from pydantic import BaseModel
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import numpy as np

# Define request schema
class RandomForestRequest(BaseModel):
    X: list   # Training features
    y: list   # Training labels
    X_test: list  # Test features
    n_estimators: int = 100
    max_depth: int | None = None

# Create router
router = APIRouter()

@router.post("/models/random_forest_demo")
def random_forest_demo(req: RandomForestRequest):
    """
    Train a Random Forest classifier and return predictions + metrics.
    """
    # Convert lists to numpy arrays
    X = np.array(req.X)
    y = np.array(req.y)
    X_test = np.array(req.X_test)

    # Train model
    model = RandomForestClassifier(
        n_estimators=req.n_estimators,
        max_depth=req.max_depth
    )
    model.fit(X, y)

    # Predictions
    predictions = model.predict(X_test)

    # Metrics (compare predictions to first slice of y if lengths match)
    metrics = {}
    if len(y) >= len(predictions):
        metrics = classification_report(
            y[:len(predictions)],
            predictions,
            output_dict=True
        )

    return {
        "predictions": predictions.tolist(),
        "metrics": metrics,
        "feature_importances": model.feature_importances_.tolist()
    }