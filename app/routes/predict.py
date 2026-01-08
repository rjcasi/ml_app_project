from fastapi import APIRouter
from services.predict_service import predict

router = APIRouter(prefix="/predict", tags=["Prediction"])

@router.post("/")
def predict_endpoint(data: dict):
    return {"prediction": predict(data)}