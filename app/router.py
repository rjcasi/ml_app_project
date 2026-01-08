from fastapi import APIRouter

# -----------------------------
# Atomic Endpoints (Math + ML)
# -----------------------------
from app.endpoints import (
    gamma,
    beta,
    zeta,
    mittag_leffler,
    random_forest,
    hash_table,
    spike_classifier
)

# -----------------------------
# Original Domain-Level Routes
# -----------------------------
from app.routes import (
    cnn,
    dsa,
    ml_algos,
    nlp,
    nn,
    optimization,
    parallel,
    rl,
    security,
    simulation,
    stats,
    timeseries,
    train,
    predict,
    evaluate,
    visualization
)

# -----------------------------
# New Organs (Added by Scaffold)
# -----------------------------
from app.routes import (
    xai,
    attention,
    cyberlab,
    generative
)

router = APIRouter()

# Atomic endpoints
router.include_router(gamma.router)
router.include_router(beta.router)
router.include_router(zeta.router)
router.include_router(mittag_leffler.router)
router.include_router(random_forest.router)
router.include_router(hash_table.router)
router.include_router(spike_classifier.router)

# Original domain routes
router.include_router(cnn.router)
router.include_router(dsa.router)
router.include_router(ml_algos.router)
router.include_router(nlp.router)
router.include_router(nn.router)
router.include_router(optimization.router)
router.include_router(parallel.router)
router.include_router(rl.router)
router.include_router(security.router)
router.include_router(simulation.router)
router.include_router(stats.router)
router.include_router(timeseries.router)
router.include_router(train.router)
router.include_router(predict.router)
router.include_router(evaluate.router)
router.include_router(visualization.router)

# New organs
router.include_router(xai.router)
router.include_router(attention.router)
router.include_router(cyberlab.router)
router.include_router(generative.router)