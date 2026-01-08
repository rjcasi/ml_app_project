from fastapi import APIRouter

router = APIRouter()
hash_table = {}

@router.post("/hash/insert")
def insert(key: str, value: str):
    hash_table[key] = value
    return {"status": "inserted", "key": key, "value": value}

@router.get("/hash/get")
def get(key: str):
    return {"key": key, "value": hash_table.get(key)}