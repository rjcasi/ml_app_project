"""
entropy_core.py
Reusable entropy and randomness functions for entropy_lab.
"""

import math
from collections import Counter
import random

# -----------------------------
# Entropy Measures
# -----------------------------

def shannon_entropy(data):
    """
    Compute Shannon entropy of a dataset.
    """
    counts = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy


def renyi_entropy(data, alpha=2):
    """
    Compute Rényi entropy of order alpha.
    Default alpha=2 gives collision entropy.
    """
    if alpha <= 0:
        raise ValueError("Alpha must be > 0")
    counts = Counter(data)
    total = len(data)
    probs = [count / total for count in counts.values()]
    return (1 / (1 - alpha)) * math.log2(sum(p ** alpha for p in probs))


def min_entropy(data):
    """
    Compute min-entropy (worst-case unpredictability).
    """
    counts = Counter(data)
    total = len(data)
    max_p = max(counts.values()) / total
    return -math.log2(max_p)


# -----------------------------
# Randomness Tests
# -----------------------------

def chi_square_uniform_test(data, alphabet=None):
    """
    Chi-square test for uniform distribution.
    Returns (chi2_stat, p_value_approx).
    """
    if alphabet is None:
        alphabet = set(data)
    counts = Counter(data)
    n = len(data)
    expected = n / len(alphabet)
    chi2 = sum(((counts[sym] - expected) ** 2) / expected for sym in alphabet)
    # Approximate p-value using survival function of chi2 distribution
    # For simplicity, return stat only; full p-value requires scipy
    return chi2


def runs_test(data):
    """
    Runs test for randomness in binary sequences.
    Returns number of runs observed.
    """
    if not all(x in [0, 1] for x in data):
        raise ValueError("Runs test requires binary data (0/1).")
    runs = 1
    for i in range(1, len(data)):
        if data[i] != data[i - 1]:
            runs += 1
    return runs


def monte_carlo_pi(samples=10000):
    """
    Monte Carlo randomness test: estimate pi using random points.
    """
    inside = 0
    for _ in range(samples):
        x, y = random.random(), random.random()
        if x*x + y*y <= 1:
            inside += 1
    return (4 * inside) / samples