#!/usr/bin/env bash

set -e

echo "🔥 Creating ML App Project scaffold..."

# -----------------------------
# Core directories
# -----------------------------
mkdir -p app/endpoints
mkdir -p app/routes
mkdir -p app/services
mkdir -p app/models
mkdir -p app/utils
mkdir -p docs/examples
mkdir -p charts
mkdir -p entropy_lab/demos
mkdir -p tests

# -----------------------------
# Core files
# -----------------------------
touch README.md
touch docker-compose.yml
touch environment.yml
touch requirements.txt
touch test_endpoints.py

# -----------------------------
# App core
# -----------------------------
cat > app/main.py << 'EOF'
from fastapi import FastAPI
from app.router import router

app = FastAPI(title="ML App Project")
app.include_router(router)
EOF

cat > app/config.py << 'EOF'
class Settings:
    PROJECT_NAME = "ML App Project"

settings = Settings()
EOF

# -----------------------------
# Router aggregator
# -----------------------------
cat > app/router.py << 'EOF'
from fastapi import APIRouter

# endpoints
from app.endpoints import (
    gamma, beta, zeta, mittag_leffler,
    random_forest, hash_table,
    spike_classifier
)

# routes
from app.routes import (
    xai, attention, cyberlab, generative
)

router = APIRouter()

# atomic endpoints
router.include_router(gamma.router)
router.include_router(beta.router)
router.include_router(zeta.router)
router.include_router(mittag_leffler.router)
router.include_router(random_forest.router)
router.include_router(hash_table.router)
router.include_router(spike_classifier.router)

# domain-level routes
router.include_router(xai.router)
router.include_router(attention.router)
router.include_router(cyberlab.router)
router.include_router(generative.router)
EOF

# -----------------------------
# Endpoints (math + ML)
# -----------------------------
cat > app/endpoints/gamma.py << 'EOF'
from fastapi import APIRouter
from scipy.special import gamma

router = APIRouter()

@router.get("/gamma")
def compute_gamma(x: float):
    return {"input": x, "gamma": float(gamma(x))}
EOF

cat > app/endpoints/beta.py << 'EOF'
from fastapi import APIRouter
from scipy.special import beta

router = APIRouter()

@router.get("/beta")
def compute_beta(a: float, b: float):
    return {"a": a, "b": b, "beta": float(beta(a, b))}
EOF

cat > app/endpoints/zeta.py << 'EOF'
from fastapi import APIRouter
from mpmath import zeta

router = APIRouter()

@router.get("/zeta")
def compute_zeta(s: float):
    return {"s": s, "zeta": float(zeta(s))}
EOF

cat > app/endpoints/mittag_leffler.py << 'EOF'
from fastapi import APIRouter
from mpmath import mittag_leffler

router = APIRouter()

@router.get("/mittag-leffler")
def compute_mittag_leffler(a: float, z: float):
    return {"a": a, "z": z, "mittag_leffler": float(mittag_leffler(a, z))}
EOF

cat > app/endpoints/random_forest.py << 'EOF'
from fastapi import APIRouter
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

router = APIRouter()

iris = load_iris()
model = RandomForestClassifier().fit(iris.data, iris.target)

@router.post("/random-forest/predict")
def predict(features: list[float]):
    pred = model.predict([features])[0]
    return {"prediction": int(pred)}
EOF

cat > app/endpoints/hash_table.py << 'EOF'
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
EOF

# -----------------------------
# New Organ: Spike Classifier
# -----------------------------
cat > app/endpoints/spike_classifier.py << 'EOF'
from fastapi import APIRouter
from app.services.spike_service import predict_spikes

router = APIRouter()

@router.post("/spike-classifier/predict")
def predict(signal: list[float]):
    return predict_spikes(signal)
EOF

cat > app/services/spike_service.py << 'EOF'
import numpy as np

def predict_spikes(signal):
    spikes = [1 if x > 0.5 else 0 for x in signal]
    return {"spikes": spikes}
EOF

# -----------------------------
# New Organ: XAI
# -----------------------------
cat > app/routes/xai.py << 'EOF'
from fastapi import APIRouter
from app.services.xai_service import feature_importance

router = APIRouter()

@router.post("/xai/importance")
def importance(data: list[list[float]], labels: list[int]):
    return feature_importance(data, labels)
EOF

cat > app/services/xai_service.py << 'EOF'
from sklearn.ensemble import RandomForestClassifier

def feature_importance(data, labels):
    model = RandomForestClassifier().fit(data, labels)
    return {"importances": model.feature_importances_.tolist()}
EOF

# -----------------------------
# New Organ: Attention Tensor
# -----------------------------
cat > app/routes/attention.py << 'EOF'
from fastapi import APIRouter
from app.services.attention_service import compute_tensor

router = APIRouter()

@router.post("/attention/visualize")
def visualize(matrix: list[list[float]], params: dict):
    return compute_tensor(matrix, params)
EOF

cat > app/services/attention_service.py << 'EOF'
import numpy as np

def compute_tensor(matrix, params):
    M = np.array(matrix)
    scale = params.get("scale", 1.0)
    return {"tensor": (M * scale).tolist()}
EOF

# -----------------------------
# New Organ: Cyberlab
# -----------------------------
cat > app/routes/cyberlab.py << 'EOF'
from fastapi import APIRouter
from app.services.cyberlab_service import fuzz, defend

router = APIRouter()

@router.post("/cyberlab/fuzz")
def fuzz_route(seed: str):
    return fuzz(seed)

@router.post("/cyberlab/defend")
def defend_route(pattern: str):
    return defend(pattern)
EOF

cat > app/services/cyberlab_service.py << 'EOF'
import random
import string

def fuzz(seed):
    random.seed(seed)
    return {"attack": ''.join(random.choices(string.ascii_letters, k=12))}

def defend(pattern):
    safe = pattern.replace("A", "*")
    return {"defended": safe}
EOF

# -----------------------------
# New Organ: Generative Playground
# -----------------------------
cat > app/routes/generative.py << 'EOF'
from fastapi import APIRouter
from app.services.generative_service import generate_text

router = APIRouter()

@router.post("/generate/text")
def text(prompt: str, temperature: float = 1.0):
    return generate_text(prompt, temperature)
EOF

cat > app/services/generative_service.py << 'EOF'
def generate_text(prompt, temperature):
    return {"generated": prompt[::-1]}
EOF

# -----------------------------
# Utils
# -----------------------------
cat > app/utils/metrics.py << 'EOF'
def accuracy(y_true, y_pred):
    return sum(int(a == b) for a, b in zip(y_true, y_pred)) / len(y_true)
EOF

cat > app/utils/preprocessing.py << 'EOF'
def normalize(x):
    m = max(x)
    return [v / m for v in x]
EOF

# -----------------------------
# Entropy Lab
# -----------------------------
cat > entropy_lab/entropy_core.py << 'EOF'
import math

def shannon_entropy(data):
    total = len(data)
    probs = [data.count(x)/total for x in set(data)]
    return -sum(p * math.log2(p) for p in probs)
EOF

cat > entropy_lab/entropy_utils.py << 'EOF'
def tokenize(text):
    return text.split()
EOF

echo "✅ Scaffold complete!"
