# Eightfold Multi-Source Candidate Data Transformer

## Overview
Pipeline that ingests structured (CSV/JSON) + unstructured (PDF/GitHub) candidate data, normalizes, merges, and projects to configurable canonical schema.

## Quick Start
```bash
pip install -r requirements.txt
python main.py samples/recruiter.csv samples/sample_resume.pdf --config configs/custom.json -o output.json
```

## Project Structure
- `main.py` - CLI entrypoint
- `transformer.py` - Core logic
- `sources/` - Parsers for each source type
- `normalizers.py` - Phones, dates, skills
- `merger.py` - Deduplication & conflict resolution
- `config.py` - Runtime projection

## Sample Inputs
Place your assignment samples in `samples/`.

## Custom Config Example
See `configs/example_config.json`.

## Demo
Run the command above and record a 2-min video showing default + custom output.

## Design Doc
See `design.pdf` (one-pager covering pipeline, decisions, tradeoffs).

**Meets all requirements**: Deterministic, robust, configurable, covers structured + unstructured sources.