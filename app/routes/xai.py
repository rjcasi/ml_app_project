from fastapi import APIRouter
from app.services.xai_service import feature_importance

router = APIRouter()

@router.post("/xai/importance")
def importance(data: list[list[float]], labels: list[int]):
    return feature_importance(data, labels)
