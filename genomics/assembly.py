"""Toy de Bruijn graph assembler for unambiguous short sequences.

Not an actual long-read assembler such as Flye and not suitable for real genomes.
"""
from collections import Counter, defaultdict

def kmers(reads: list[str], k: int) -> Counter[str]:
    if k < 2: raise ValueError("k must be >= 2")
    out = Counter()
    for read in reads:
        read = read.upper()
        if any(c not in "ACGT" for c in read): raise ValueError("ACGT reads only")
        out.update(read[i:i+k] for i in range(len(read)-k+1))
    return out

def contigs_from_kmers(reads: list[str], k: int) -> list[str]:
    """Return maximal non-branching paths; cycles are not resolved."""
    counts = kmers(reads, k)
    edges = defaultdict(list)
    indeg, outdeg = Counter(), Counter()
    for word in sorted(counts):
        left, right = word[:-1], word[1:]
        edges[left].append(right)
        outdeg[left] += 1; indeg[right] += 1
    paths = []
    for start in sorted(set(indeg) | set(outdeg)):
        if outdeg[start] and (indeg[start] != 1 or outdeg[start] != 1):
            for nxt in edges[start]:
                s, cur = start + nxt[-1], nxt
                while indeg[cur] == 1 and outdeg[cur] == 1:
                    cur = edges[cur][0]
                    s += cur[-1]
                paths.append(s)
    return sorted(paths)
