from fastapi import APIRouter
from mpmath import mittag_leffler

router = APIRouter()

@router.get("/mittag-leffler")
def compute_mittag_leffler(a: float, z: float):
    return {"a": a, "z": z, "mittag_leffler": float(mittag_leffler(a, z))}