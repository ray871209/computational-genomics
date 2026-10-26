# Computational Genomics | Educational Python Portfolio

A small, reproducible **post-course portfolio adaptation** of core computational-genomics concepts encountered in the University of Melbourne **COMP90016 Computational Genomics** workshops (2024). It demonstrates basic data handling across common genomics formats, using **new Python code and exclusively fictional synthetic data**.

> **Provenance:** This repository is not the student's original workshop archive, assessed notebooks, or a reproduction of university assignments. These demonstration programs and tests were newly prepared with AI assistance after the course, drawing on general subject themes. It does not contain classroom materials, other students' work, restricted datasets, identifiable student records or solution notebooks.

## What is included

| Module | Demonstration | What it does *not* claim |
|---|---|---|
| `sequence.py` | Reverse complement, GC fraction, k-mer counts | No ambiguous-base support or genomic feature annotation |
| `fastq_qc.py` | FASTQ read parsing, mean Phred, Q20 and GC summary | Not a replacement for FastQC/NanoPlot |
| `variants.py` | Single-allele VCF variant-type summary | Not a variant caller or clinical interpretation system |
| `metagenomics.py` | Parse a small Kraken2-style six-column report | Does not run Kraken2 or classify reads |
| `single_cell_qc.py` | Per-cell total counts, detected genes, mitochondrial fraction | Not a single-cell RNA-seq processing pipeline |

The original coursework also exposed tools such as read alignment, assembly, phylogenetics, annotation and single-cell workflows. Those are **documented as topics studied**, not presented as fully implemented or rerun pipelines here.

## Run locally

Requires Python 3.10+; **standard library only**.

```bash
python -m genomics.cli
python -m unittest discover -s tests -v
```

Run from the repository root. All bundled inputs under `data/` are fabricated examples, with no biological or clinical meaning. The FASTQ example assumes Phred+33 encoding; VCF reader processes simple tab-delimited records and classifies multiallelic/symbolic records as `other_or_multiallelic`. The Kraken report demo covers the familiar six-column Kraken2 report layout, not arbitrary taxonomic result formats.

## Scope and possible extensions

This project is intentionally a **small foundational showcase** rather than a claim of end-to-end computational-genomics pipeline development. Reasonable next steps include adding a fully reproducible public-data QC case study, proper workflow environments, provenance and reference accession IDs, benchmark/validation outputs, and documented variant-calling or single-cell analysis with dedicated bioinformatics tools.

## Academic integrity and licensing

Only newly authored teaching demonstrations are bundled; university-provided assessment questions, example solutions, workshop notebooks, training datasets, and personal information have been excluded. Confirm the applicable university course rules before making this public. No third-party course material is licensed or redistributed here.
