from fastapi import APIRouter
import hashlib

router = APIRouter(prefix="/security", tags=["Security"])

@router.get("/ping")
def ping():
    return {"message": "Cybersecurity router is alive"}

@router.post("/hash")
def hash_text(text: str, algo: str = "sha256"):
    h = hashlib.new(algo)
    h.update(text.encode("utf-8"))
    return {"algorithm": algo, "hash": h.hexdigest()}
