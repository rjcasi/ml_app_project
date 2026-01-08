import numpy as np

def predict_spikes(signal):
    spikes = [1 if x > 0.5 else 0 for x in signal]
    return {"spikes": spikes}
