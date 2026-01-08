from fastapi import APIRouter
from pydantic import BaseModel
from mpmath import zeta

# Define request schema
class ZetaRequest(BaseModel):
    s: float  # input value for zeta(s)

# Create router
router = APIRouter()

@router.get("/special/zeta_function")
def zeta_function(s: float):
    """
    Compute the Riemann Zeta function ζ(s).
    """
    value = zeta(s)
    return {"input": s, "zeta(s)": str(value)}