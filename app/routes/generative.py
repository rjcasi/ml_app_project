from fastapi import APIRouter
from app.services.generative_service import generate_text

router = APIRouter()

@router.post("/generate/text")
def text(prompt: str, temperature: float = 1.0):
    return generate_text(prompt, temperature)
