from fastapi import APIRouter

router = APIRouter(prefix="/parallel", tags=["Parallel Computing"])

@router.get("/ping")
def ping():
    return {"message": "Parallel Computing router is alive"}