from fastapi import APIRouter

router = APIRouter(prefix="/nn", tags=["Neural Networks"])

@router.get("/ping")
def ping():
    return {"message": "Neural Networks router is alive"}