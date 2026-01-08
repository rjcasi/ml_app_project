def normalize(x):
    m = max(x)
    return [v / m for v in x]
