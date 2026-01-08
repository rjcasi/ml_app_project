from fastapi import APIRouter
from scipy.special import beta

router = APIRouter()

@router.get("/beta")
def compute_beta(a: float, b: float):
    return {"a": a, "b": b, "beta": float(beta(a, b))}