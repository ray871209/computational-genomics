"""Tests for extended educational modules."""
import unittest
from genomics.alignment import global_align
from genomics.assembly import kmers, contigs_from_kmers
from genomics.phylogenetics import p_distance, distance_matrix
from genomics.annotation import forward_orfs
from genomics.read_mapping import exact_matches

class ExtendedTests(unittest.TestCase):
    def test_align_exact(self):
        self.assertEqual(global_align("ACGT", "ACGT"), ("ACGT", "ACGT", 8))
    def test_align_indel(self):
        a, b, score = global_align("ACGT", "AGT")
        self.assertEqual(len(a), len(b))
        self.assertEqual(a.replace("-", ""), "ACGT")
        self.assertEqual(b.replace("-", ""), "AGT")
    def test_kmers(self):
        self.assertEqual(kmers(["ACGTA"], 3)["ACG"], 1)
        self.assertIn("ACGTA", contigs_from_kmers(["ACGTA"], 3))
    def test_distance(self):
        self.assertAlmostEqual(p_distance("ACGT", "ATGT"), 0.25)
        self.assertAlmostEqual(distance_matrix({"x":"AAAA","y":"AAAT"})["y"]["x"], 0.25)
    def test_orf(self):
        self.assertEqual(forward_orfs("CCCATGAAATTTTAACCC")[0], {"start":3,"end":15,"aa_length":3})
    def test_mapping(self):
        self.assertEqual(exact_matches("ACGTACGT", "ACG"), [0,4])
    def test_validation(self):
        with self.assertRaises(ValueError): p_distance("AC", "A")
        with self.assertRaises(ValueError): kmers(["ACT"], 1)
if __name__ == "__main__": unittest.main()
