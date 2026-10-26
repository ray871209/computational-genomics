# Computational Genomics | Python Portfolio

Independent, **AI-assisted educational implementations** of genomics data processing and algorithm concepts. This portfolio was developed after prior coursework and uses newly authored Python demonstrations plus synthetic example data. It is **not** a copy of graded assignments or workshop notebooks.

## Implemented modules

| Module | Contents | Scope |
| --- | --- | --- |
| `genomics/sequence.py` | Reverse complement, GC fraction, k-mer counts | Sequence utilities |
| `genomics/fastq_qc.py` | FASTQ parsing, Q20, Phred quality, GC | Simplified read QC |
| `genomics/variants.py` | VCF parsing, variant classification | File analysis, not variant calling |
| `genomics/metagenomics.py` | Kraken2-style report summarization | Report parsing only |
| `genomics/single_cell_qc.py` | Per-cell RNA count and mitochondrial metrics | QC only |
| `genomics/alignment.py` | Needleman–Wunsch global DNA alignment | Educational dynamic programming |
| `genomics/read_mapping.py` | Exact-match positions on a reference | No approximate mapping |
| `genomics/assembly.py` | k-mers and maximal nonbranching de Bruijn paths | Toy assembler; unresolved cycles |
| `genomics/phylogenetics.py` | Pairwise aligned DNA p-distance matrix | No inferred phylogenetic tree |
| `genomics/annotation.py` | Forward-strand ATG-to-stop ORF enumeration | Not genome annotation software |

## Workflow notes

`docs/workflows.md` outlines six broader analysis workflows, including short-read QC/mapping and variant analysis, long-read assembly, phylogenetics, genome annotation, metagenomics and single-cell RNA-seq. **These are conceptual notes, not executable workflows**. `docs/limitations.md` documents project scope.

## Run

Python 3.10+; standard library only.

```bash
python -m genomics.cli
python -m unittest discover -s tests -v
```

Examples in `data/` are fully synthetic. `tests/test_examples.py` checks the original five demonstrations; `tests/test_extended.py` checks the added algorithm modules. Run both with the command above.

## Provenance and limitations

Created for technical portfolio demonstration after studying general computational-genomics topics. Code, illustrative data, documentation, and tests were prepared with AI assistance. **This is not an original submission archive**, and the implementation should not be represented as professional production pipelines or verified laboratory methods.

No assessment questions, provided workshop data, instructor solutions, personal identifiers, or third-party materials are redistributed. No clinical interpretations are supported. No claim is made that FastQC, Snippy, Flye, QUAST, Prokka, BLAST, IQ-TREE2, Kraken2 or Seurat were run as part of this repository. See `PROJECT_NOTES.md` for details.
