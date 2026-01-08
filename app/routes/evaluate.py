# app/routes/evaluate.py
from fastapi import APIRouter
from services.evaluate_service import evaluate_classifier

router = APIRouter(prefix="/evaluate", tags=["Evaluation"])

@router.get("/")
def evaluate_endpoint():
    return evaluate_classifier()