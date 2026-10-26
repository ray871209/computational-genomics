"""Exact-match read placement against a reference (toy mapping demonstration).

Not an alignment pipeline, variant caller, mapper or substitute for Snippy.
"""
def exact_matches(reference: str, read: str) -> list[int]:
    reference, read = reference.upper(), read.upper()
    if not read or any(x not in "ACGT" for x in reference + read):
        raise ValueError("Nonempty ACGT read and ACGT reference required")
    positions, start = [], 0
    while True:
        pos = reference.find(read, start)
        if pos < 0: return positions
        positions.append(pos)
        start = pos + 1
