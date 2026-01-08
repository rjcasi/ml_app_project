from fastapi import APIRouter

router = APIRouter(prefix="/cnn", tags=["CNN"])

@router.get("/ping")
def ping():
    return {"message": "CNN router is alive"}