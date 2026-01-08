from fastapi import APIRouter

router = APIRouter(prefix="/optimization", tags=["Optimization"])

@router.get("/ping")
def ping():
    return {"message": "Optimization router is alive"}

@router.post("/gradient_descent")
def gradient_descent(start: float, lr: float = 0.1, epochs: int = 10):
    x = start
    history = []
    for _ in range(epochs):
        grad = 2 * x  # derivative of f(x) = x^2
        x -= lr * grad
        history.append(x)
    return {"method": "Gradient Descent", "final": x, "history": history}