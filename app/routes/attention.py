from fastapi import APIRouter
from app.services.attention_service import compute_tensor

router = APIRouter()

@router.post("/attention/visualize")
def visualize(matrix: list[list[float]], params: dict):
    return compute_tensor(matrix, params)
