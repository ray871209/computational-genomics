"""Small VCF summary, not a variant caller or clinical annotation workflow."""
from collections import Counter
from pathlib import Path

def summarize_vcf(path: str | Path) -> dict:
    variant_types = Counter()
    records = 0
    with open(path, encoding='utf-8') as fh:
        for line in fh:
            if line.startswith('#'):
                continue
            parts = line.rstrip('\n').split('\t')
            if len(parts) < 8:
                raise ValueError('VCF requires at least eight columns')
            ref, alt = parts[3], parts[4]
            if alt == '.' or ',' in alt or ref.startswith('<') or alt.startswith('<'):
                variant_types['other_or_multiallelic'] += 1
            elif len(ref) == len(alt) == 1:
                variant_types['SNV'] += 1
            elif len(ref) == len(alt):
                variant_types['MNV'] += 1
            elif len(ref) < len(alt):
                variant_types['insertion'] += 1
            else:
                variant_types['deletion'] += 1
            records += 1
    return {'records': records, 'classes': dict(variant_types)}
