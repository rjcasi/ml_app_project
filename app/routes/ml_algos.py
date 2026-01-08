from fastapi import APIRouter

router = APIRouter(prefix="/ml_algos", tags=["ML Algorithms"])

@router.get("/ping")
def ping():
    return {"message": "ML Algorithms router is alive"}