# Eightfold Multi-Source Candidate Data Transformer

Pipeline that ingests candidate data from structured and unstructured sources, normalizes, merges duplicates, and outputs a clean canonical profile with provenance and runtime-configurable projection.

## Features
- Supports structured (CSV, JSON) + unstructured (PDF, GitHub) sources
- Normalization (phones E.164, canonical skills)
- Merging with confidence-based conflict resolution
- Runtime configurable output (field selection, rename, normalization)
- Robust & deterministic

## Quick Start

```bash
pip install -r requirements.txt
```
```bash
Default run:
Bashpython -m main samples/sample_recruiter.csv samples/your_resume.pdf
```
With custom config:
Bashpython -m main samples/sample_recruiter.csv --config configs/example_config.json --output outputs/custom.json
Project Structure

main.py — CLI interface
transformer.py — Core pipeline
sources/ — Parsers for each source type
normalizers.py — Data cleaning
merger.py — Deduplication
config.py — Runtime projection
