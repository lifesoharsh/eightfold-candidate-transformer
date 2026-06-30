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
Default run:
```bash
python -m main samples/sample_recruiter.csv samples/your_resume.pdf
```
With custom config:
```bash
python -m main samples/sample_recruiter.csv --config configs/example_config.json --output outputs/custom.json
```
## Project Structure

```bash
candidate-transformer/
├── main.py                 # CLI entrypoint
├── transformer.py          # Core pipeline logic
├── config.py               # Runtime output projection
├── normalizers.py          # Data normalization (phones, skills, etc.)
├── merger.py               # Profile merging & conflict resolution
├── sources/
│   ├── base.py
│   ├── recruiter_csv.py
│   ├── ats_json.py
│   ├── resume_pdf.py
│   └── github.py
├── configs/
│   └── example_config.json
├── samples/                # Put assignment input files here
├── outputs/                # Generated results
└── README.md
