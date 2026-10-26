"""Simple Hamming/p-distance utilities for aligned DNA sequences.

These functions do not run IQ-TREE or infer a maximum-likelihood phylogeny.
"""
from itertools import combinations

def p_distance(a: str, b: str) -> float:
    if len(a) != len(b) or not a:
        raise ValueError("Aligned sequences must have matching positive length")
    valid = [(x, y) for x, y in zip(a.upper(), b.upper())
             if x in "ACGT" and y in "ACGT"]
    if not valid: raise ValueError("No comparable non-gap DNA sites")
    return sum(x != y for x, y in valid) / len(valid)

def distance_matrix(sequences: dict[str, str]) -> dict[str, dict[str, float]]:
    if len(sequences) < 2: raise ValueError("Need at least two sequences")
    labels = sorted(sequences)
    result = {name: {other: 0.0 for other in labels} for name in labels}
    for a, b in combinations(labels, 2):
        d = p_distance(sequences[a], sequences[b])
        result[a][b] = result[b][a] = d
    return result
