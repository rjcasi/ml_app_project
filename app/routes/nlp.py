from fastapi import APIRouter

router = APIRouter(prefix="/nlp", tags=["NLP"])

@router.get("/ping")
def ping():
    return {"message": "NLP router is alive"}