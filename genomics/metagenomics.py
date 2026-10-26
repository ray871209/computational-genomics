"""Summarise the simplified, tab-separated Kraken2 report format."""
import csv
from pathlib import Path

def species_in_report(path: str | Path) -> list[dict]:
    out = []
    with open(path, encoding='utf-8', newline='') as fh:
        reader = csv.reader(fh, delimiter='\t')
        for row in reader:
            if len(row) != 6:
                raise ValueError('Expected six columns in Kraken2-style report')
            percent, clade, direct, rank, taxid, name = row
            if rank.strip() == 'S':
                out.append({'taxon': name.strip(), 'taxid': taxid.strip(),
                            'clade_reads': int(clade), 'direct_reads': int(direct),
                            'percent': float(percent)})
    return sorted(out, key=lambda r: -r['clade_reads'])
