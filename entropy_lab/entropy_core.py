import math

def shannon_entropy(data):
    total = len(data)
    probs = [data.count(x) / total for x in set(data)]
    return -sum(p * math.log2(p) for p in probs)