# app/main.py
from fastapi import FastAPI
from app.routes import (
    stats,
    ml_algos,
    nn,
    rl,
    cnn,
    nlp,
    timeseries,
    optimization,
    simulation,
    parallel,
    security,
    visualization,
    dsa,   # <-- newly added DS&A router
)

app = FastAPI(title="Renzo's ML & DS Cockpit API 🚀")

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to Renzo's ML & DS Cockpit API 🚀"}

# Include routers
app.include_router(stats.router)
app.include_router(ml_algos.router)
app.include_router(nn.router)
app.include_router(rl.router)
app.include_router(cnn.router)
app.include_router(nlp.router)
app.include_router(timeseries.router)
app.include_router(optimization.router)
app.include_router(simulation.router)
app.include_router(parallel.router)
app.include_router(security.router)
app.include_router(visualization.router)
app.include_router(dsa.router)   # <-- DS&A endpoints now live