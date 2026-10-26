"""Simplified ORF prediction on the forward DNA strand, genetic code 11-style start ATG.

An educational example: no gene model, overlapping-strand inference or Prokka run.
"""
STOP = {"TAA", "TAG", "TGA"}

def forward_orfs(sequence: str, min_aa: int = 2) -> list[dict[str, int]]:
    """Find ATG-to-stop ORFs; 0-based start and half-open end positions."""
    seq = sequence.upper()
    if any(x not in "ACGT" for x in seq): raise ValueError("ACGT sequence only")
    if min_aa < 1: raise ValueError("min_aa must be positive")
    found = []
    for frame in range(3):
        for start in range(frame, len(seq)-2, 3):
            if seq[start:start+3] != "ATG": continue
            for pos in range(start+3, len(seq)-2, 3):
                if seq[pos:pos+3] in STOP:
                    aa = (pos-start)//3
                    if aa >= min_aa:
                        found.append({"start": start, "end": pos+3, "aa_length": aa})
                    break
    return sorted(found, key=lambda x: (x["start"], x["end"]))
