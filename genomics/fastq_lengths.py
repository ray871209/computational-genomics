"""Simple FASTQ read-length distribution and N50, for educational data QC.

N50 is a length-distribution statistic, not evidence of assembly correctness.
"""
from pathlib import Path
from genomics.fastq_qc import read_fastq

def n50(lengths: list[int]) -> int:
    if not lengths:
        return 0
    if any(length < 0 for length in lengths):
        raise ValueError("Read lengths cannot be negative")
    total = sum(lengths)
    if not total:
        return 0
    cumulative = 0
    for length in sorted(lengths, reverse=True):
        cumulative += length
        if cumulative * 2 >= total:
            return length
    return 0

def summarize_lengths(path: str | Path) -> dict:
    lengths = [len(sequence) for _, sequence, _ in read_fastq(path)]
    if not lengths:
        return {"reads": 0, "mean_length": 0.0, "min_length": 0, "max_length": 0, "read_n50": 0}
    return {
        "reads": len(lengths),
        "mean_length": round(sum(lengths) / len(lengths), 2),
        "min_length": min(lengths),
        "max_length": max(lengths),
        "read_n50": n50(lengths),
    }
