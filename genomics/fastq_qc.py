"""Minimal FASTQ parsing and descriptive per-read QC (Phred+33)."""
from pathlib import Path

def read_fastq(path: str | Path):
    with open(path, encoding='utf-8') as fh:
        while True:
            header = fh.readline()
            if not header:
                return
            sequence, plus, quality = fh.readline(), fh.readline(), fh.readline()
            if not all((sequence, plus, quality)) or not header.startswith('@') or not plus.startswith('+'):
                raise ValueError('Malformed FASTQ record')
            sequence, quality = sequence.strip().upper(), quality.strip()
            if len(sequence) != len(quality) or any(ord(q) < 33 or ord(q) > 126 for q in quality):
                raise ValueError('Invalid sequence/quality encoding')
            yield header[1:].strip(), sequence, [ord(q)-33 for q in quality]

def summarize_fastq(path: str | Path) -> dict:
    count = 0
    total_bases = total_q = gc = q20 = 0
    for _, seq, scores in read_fastq(path):
        count += 1
        total_bases += len(seq)
        total_q += sum(scores)
        gc += sum(b in 'GC' for b in seq)
        q20 += sum(q >= 20 for q in scores)
    return {'reads': count, 'bases': total_bases,
            'mean_length': round(total_bases/count, 2) if count else 0,
            'mean_phred': round(total_q/total_bases, 2) if total_bases else 0,
            'q20_fraction': round(q20/total_bases, 4) if total_bases else 0,
            'gc_fraction': round(gc/total_bases, 4) if total_bases else 0}
