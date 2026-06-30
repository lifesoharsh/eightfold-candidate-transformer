import json
from pathlib import Path
from typing import Dict, Any
from .base import SourceParser
from normalizers import normalize_phone

class ATSJSONParser(SourceParser):
    def parse(self, file_path: Path) -> Dict[str, Any]:
        with open(file_path) as f:
            data = json.load(f)
        
        # Assume semi-structured
        profile = {
            "candidate_id": data.get("candidate_id", "unknown"),
            "full_name": data.get("full_name", ""),
            "emails": data.get("emails", []),
            "phones": [normalize_phone(p) for p in data.get("phones", [])],
            "headline": data.get("title", ""),
            "provenance": [{"field": "all", "source": "ats_json", "method": "direct"}],
            "overall_confidence": 0.85
        }
        return profile