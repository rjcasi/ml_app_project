from fastapi import APIRouter
from app.services.cyberlab_service import fuzz, defend

router = APIRouter()

@router.post("/cyberlab/fuzz")
def fuzz_route(seed: str):
    return fuzz(seed)

@router.post("/cyberlab/defend")
def defend_route(pattern: str):
    return defend(pattern)
