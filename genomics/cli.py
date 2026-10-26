"""Run representative demonstrations with bundled synthetic data."""
import json
from pathlib import Path
from .sequence import reverse_complement, gc_fraction, kmers
from .fastq_qc import summarize_fastq
from .variants import summarize_vcf
from .metagenomics import species_in_report
from .single_cell_qc import cell_qc

DATA = Path(__file__).resolve().parents[1] / 'data'

def main():
    report = {
        'sequence': {'reverse_complement': reverse_complement('ATGCCGTA'),
                     'gc_fraction': gc_fraction('ATGCCGTA'), 'dinucleotides': kmers('ATGCCGTA', 2)},
        'fastq_qc': summarize_fastq(DATA/'synthetic_reads.fastq'),
        'vcf': summarize_vcf(DATA/'synthetic_variants.vcf'),
        'metagenomics_species': species_in_report(DATA/'synthetic_kraken_report.tsv'),
        'single_cell_qc': cell_qc(DATA/'synthetic_cell_counts.csv')
    }
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
