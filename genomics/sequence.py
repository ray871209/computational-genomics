"""Basic DNA transformations; assumes unambiguous A/C/G/T input."""
from collections import Counter

_COMPLEMENT = str.maketrans('ACGT', 'TGCA')

def validate_dna(sequence: str) -> str:
    seq = sequence.upper().strip()
    if any(base not in 'ACGT' for base in seq):
        raise ValueError('Only A/C/G/T DNA bases are supported')
    return seq

def reverse_complement(sequence: str) -> str:
    return validate_dna(sequence).translate(_COMPLEMENT)[::-1]

def gc_fraction(sequence: str) -> float:
    seq = validate_dna(sequence)
    return sum(base in 'GC' for base in seq) / len(seq) if seq else 0.0

def kmers(sequence: str, k: int) -> dict[str, int]:
    seq = validate_dna(sequence)
    if k <= 0:
        raise ValueError('k must be positive')
    return dict(Counter(seq[i:i+k] for i in range(len(seq)-k+1)))
