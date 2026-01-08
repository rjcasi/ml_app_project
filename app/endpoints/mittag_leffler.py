from fastapi import APIRouter
from pydantic import BaseModel
from mpmath import mittag_leffler

# Define request schema
class MittagLefflerRequest(BaseModel):
    alpha: float   # order parameter (α > 0)
    z: float       # argument (real number for now)
    terms: int = 50  # number of series terms to approximate

# Create router
router = APIRouter()

@router.get("/special/mittag_leffler")
def mittag_leffler_function(alpha: float, z: float, terms: int = 50):
    """
    Compute the Mittag-Leffler function E_alpha(z).
    For alpha=1, this reduces to exp(z).
    """
    value = mittag_leffler(alpha, 1, z, terms)  # E_alpha(z) with beta=1
    return {"alpha": alpha, "z": z, "E_alpha(z)": str(value)}