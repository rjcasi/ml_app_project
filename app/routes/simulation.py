from fastapi import APIRouter
import random

router = APIRouter(prefix="/simulation", tags=["Simulation"])

@router.get("/ping")
def ping():
    return {"message": "Simulation router is alive"}

@router.get("/pi")
def monte_carlo_pi(trials: int = 1000):
    inside = 0
    for _ in range(trials):
        x, y = random.random(), random.random()
        if x*x + y*y <= 1:
            inside += 1
    estimate = 4 * inside / trials
    return {"method": "Monte Carlo Pi", "trials": trials, "estimate": estimate}