from fastapi import APIRouter
from app.services.spike_service import predict_spikes

router = APIRouter()

@router.post("/spike-classifier/predict")
def predict(signal: list[float]):
    return predict_spikes(signal)
