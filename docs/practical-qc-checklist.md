# Computational genomics practical QC checklist

This document adds interpretation and reproducibility considerations to the synthetic educational code. It does not claim that external bioinformatics tools were run.

## Sequencing QC
- Document instrument, chemistry, basecaller, reference assembly and software versions.
- FASTQ stores sequences and Phred-encoded qualities; Q20 corresponds to a nominal 1% error probability when calibrated.
- Check base quality, adapter contamination, read length distribution and GC jointly.
- For long reads also record length N50 and mapping/consensus metrics.

## Variant analysis
- Preserve VCF header, reference build, contig names and FILTER interpretation.
- Parsing a VCF is distinct from calling variants or validating them experimentally.
- Normalize indels when comparing records; depth and allele balance are context dependent.

## Assembly and annotation
- N50 is not proof of assembly accuracy; check completeness, contamination and read support.
- The toy de Bruijn code does not resolve repetitive genomes or sequencing errors.
- The ORF demonstration is not equivalent to a full gene annotation pipeline.

## Metagenomics and single cell
- Kraken-style results depend heavily on database content and version; negative controls matter.
- Single-cell QC thresholds depend on tissue and experiment; downstream interpretation requires replicates and appropriate normalization.

## Limitations
All bundled examples use synthetic input and are not clinical or production-ready.
