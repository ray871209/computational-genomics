"""Tests for the independent read-length QC example."""
import unittest
from pathlib import Path
from genomics.fastq_lengths import n50, summarize_lengths

class LengthTests(unittest.TestCase):
    def test_n50(self):
        self.assertEqual(n50([10, 5, 5]), 10)
        self.assertEqual(n50([]), 0)
        self.assertEqual(n50([0, 0]), 0)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            n50([-1, 2])

    def test_synthetic_fastq(self):
        path = Path(__file__).resolve().parents[1] / "data" / "synthetic_reads.fastq"
        result = summarize_lengths(path)
        self.assertGreater(result["reads"], 0)
        self.assertGreaterEqual(result["max_length"], result["read_n50"])

if __name__ == "__main__":
    unittest.main()
