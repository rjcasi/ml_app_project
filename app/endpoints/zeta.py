from fastapi import APIRouter
from mpmath import zeta

router = APIRouter()

@router.get("/zeta")
def compute_zeta(s: float):
    return {"s": s, "zeta": float(zeta(s))}