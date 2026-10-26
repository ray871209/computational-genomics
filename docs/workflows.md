# Genomics workflows: study notes

These are **conceptual workflow outlines**, not claims that the accompanying repository executes third-party tools. Commands here are deliberately omitted because a real pipeline needs dataset-specific parameters, versions, reference genomes and provenance.

## Short-read QC and mapping
FASTQ → per-base and per-read QC (e.g. FastQC) → read filtering/trimming when appropriate → reference mapping → alignment QC → variant identification → filtered VCF → manual/biological interpretation.

## Long-read assembly
Basecalled FASTQ → read length/quality summaries (e.g. NanoPlot) → assembly (e.g. Flye) → polishing as appropriate → contig quality metrics (e.g. QUAST) → contamination/completeness checks.

## Phylogenetic inference
Homologous sequences → multiple sequence alignment → trimming or masking where justified → model selection/tree inference (e.g. IQ-TREE2) → branch support → tree visualization. This project's p-distance module is **not** a replacement for phylogenetic inference.

## Genome annotation
Assembly → structural and functional gene annotation (e.g. Prokka for bacteria) → standardized naming and database comparisons → lineage/MLST or BLAST analysis as appropriate.

## Metagenomics
FASTQ QC → taxonomic classification (e.g. Kraken2) → abundance summary → contamination controls and database-version assessment → visualization and interpretation. The existing parser only summarizes tabular output; it does **not** classify reads.

## Single-cell RNA-seq
Count matrix → per-cell gene/count/mitochondrial QC → doublet assessment → normalization → dimensionality reduction → clustering → cell-type annotation → differential expression with appropriate replication. The existing code only demonstrates QC metrics.
