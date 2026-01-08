# app/routes/train.py
from fastapi import APIRouter
from services.train_service import train_classifier

router = APIRouter(prefix="/train", tags=["Training"])

@router.post("/")
def train_endpoint():
    return train_classifier()