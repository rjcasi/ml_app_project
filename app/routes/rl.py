from fastapi import APIRouter

router = APIRouter(prefix="/rl", tags=["Reinforcement Learning"])

@router.get("/ping")
def ping():
    return {"message": "Reinforcement Learning router is alive"}