from fastapi import APIRouter
from scipy.special import gamma

router = APIRouter()

@router.get("/gamma")
def compute_gamma(x: float):
    return {"input": x, "gamma": float(gamma(x))}