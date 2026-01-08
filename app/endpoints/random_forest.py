from fastapi import APIRouter
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

router = APIRouter()

iris = load_iris()
model = RandomForestClassifier().fit(iris.data, iris.target)

@router.post("/random-forest/predict")
def predict(features: list[float]):
    pred = model.predict([features])[0]
    return {"prediction": int(pred)}