"""Global pairwise alignment with an explicit Needleman-Wunsch DP table.

Educational algorithm demonstration; not a replacement for a read aligner.
"""
def global_align(reference: str, query: str, match: int = 2,
                 mismatch: int = -1, gap: int = -2) -> tuple[str, str, int]:
    if not all(c in "ACGTN" for c in (reference + query).upper()):
        raise ValueError("Only DNA symbols A/C/G/T/N are supported")
    a, b = reference.upper(), query.upper()
    n, m = len(a), len(b)
    score = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): score[i][0] = i * gap
    for j in range(1, m + 1): score[0][j] = j * gap
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            score[i][j] = max(
                score[i-1][j-1] + (match if a[i-1] == b[j-1] else mismatch),
                score[i-1][j] + gap, score[i][j-1] + gap)
    x, y, i, j = [], [], n, m
    while i or j:
        if i and j and score[i][j] == score[i-1][j-1] + (match if a[i-1] == b[j-1] else mismatch):
            x.append(a[i-1]); y.append(b[j-1]); i -= 1; j -= 1
        elif i and score[i][j] == score[i-1][j] + gap:
            x.append(a[i-1]); y.append("-"); i -= 1
        else:
            x.append("-"); y.append(b[j-1]); j -= 1
    return "".join(reversed(x)), "".join(reversed(y)), score[n][m]
