import unittest
from pathlib import Path
from genomics.sequence import gc_fraction, kmers, reverse_complement
from genomics.fastq_qc import summarize_fastq
from genomics.variants import summarize_vcf
from genomics.metagenomics import species_in_report
from genomics.single_cell_qc import cell_qc
D = Path(__file__).resolve().parents[1] / 'data'

class GenomicsTests(unittest.TestCase):
    def test_reverse_complement(self): self.assertEqual(reverse_complement('AtGc'), 'GCAT')
    def test_invalid_base(self):
        with self.assertRaises(ValueError): reverse_complement('ATN')
    def test_gc(self): self.assertAlmostEqual(gc_fraction('ACGC'), .75)
    def test_kmers(self): self.assertEqual(kmers('AAAA', 2), {'AA': 3})
    def test_fastq(self):
        result = summarize_fastq(D/'synthetic_reads.fastq')
        self.assertEqual((result['reads'], result['bases']), (3, 24))
        self.assertEqual(result['q20_fraction'], 1.0)
    def test_vcf(self):
        self.assertEqual(summarize_vcf(D/'synthetic_variants.vcf')['classes'],
                         {'SNV': 1, 'insertion': 1, 'deletion': 1, 'MNV': 1})
    def test_kraken(self):
        rows = species_in_report(D/'synthetic_kraken_report.tsv')
        self.assertEqual([r['clade_reads'] for r in rows], [22, 10])
    def test_cell_qc(self):
        cells = cell_qc(D/'synthetic_cell_counts.csv')
        self.assertEqual(cells[0]['detected_genes'], 3)
        self.assertEqual(cells[1]['mitochondrial_fraction'], .5)

if __name__ == '__main__': unittest.main()
