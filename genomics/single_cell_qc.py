"""Demonstration of simple per-cell QC from a tiny cell-by-gene count CSV.

This is NOT a replacement for Scanpy/Seurat; no filtering thresholds are imposed.
"""
import csv
from pathlib import Path

def cell_qc(path: str | Path) -> list[dict]:
    with open(path, encoding='utf-8', newline='') as fh:
        rows = csv.DictReader(fh)
        if not rows.fieldnames or rows.fieldnames[0] != 'cell_id':
            raise ValueError('First column must be cell_id')
        genes = rows.fieldnames[1:]
        results = []
        for row in rows:
            counts = [int(row[g]) for g in genes]
            if any(n < 0 for n in counts):
                raise ValueError('Counts must be nonnegative')
            total = sum(counts)
            mito = sum(int(row[g]) for g in genes if g.upper().startswith('MT-'))
            results.append({'cell_id': row['cell_id'], 'total_counts': total,
                            'detected_genes': sum(n > 0 for n in counts),
                            'mitochondrial_fraction': round(mito/total, 4) if total else 0.0})
        return results
