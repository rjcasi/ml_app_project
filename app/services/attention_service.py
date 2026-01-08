import numpy as np

def compute_tensor(matrix, params):
    M = np.array(matrix)
    scale = params.get("scale", 1.0)
    return {"tensor": (M * scale).tolist()}
