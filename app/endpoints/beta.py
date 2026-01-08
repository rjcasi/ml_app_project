from fastapi import APIRouter
from pydantic import BaseModel
from scipy.special import beta, gamma

# Define request schema
class BetaRequest(BaseModel):
    x: float
    y: float

# Create router
router = APIRouter()

@router.get("/special/beta_function")
def beta_function(x: float, y: float):
    """
    Compute the Beta function B(x,y) and show its relation to Gamma.
    """
    value = beta(x, y)
    relation = (gamma(x) * gamma(y)) / gamma(x + y)
    return {
        "inputs": {"x": x, "y": y},
        "B(x,y)": value,
        "Gamma_relation": relation
    }