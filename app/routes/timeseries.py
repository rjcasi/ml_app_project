from fastapi import APIRouter

router = APIRouter(prefix="/timeseries", tags=["Time Series"])

@router.get("/ping")
def ping():
    return {"message": "Time Series router is alive"}

@router.post("/moving_average")
def moving_average(values: list[int], window: int):
    result = []
    for i in range(len(values) - window + 1):
        result.append(sum(values[i:i+window]) / window)
    return {"method": "Moving Average", "result": result}