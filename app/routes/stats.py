from fastapi import APIRouter

router = APIRouter(prefix="/stats", tags=["Statistics"])

@router.get("/ping")
def ping():
    return {"message": "Stats router is alive"}