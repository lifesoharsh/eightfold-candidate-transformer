import pandas as pd
from pathlib import Path
from typing import Dict, Any
from .base import SourceParser
from normalizers import normalize_phone, normalize_location

class RecruiterCSVParser(SourceParser):
    def parse(self, file_path: Path) -> Dict[str, Any]:
        df = pd.read_csv(file_path)
        if df.empty:
            return {}
        
        row = df.iloc[0].fillna('').to_dict()
        
        profile = {
            "candidate_id": str(row.get("id", row.get("candidate_id", "unknown"))),
            "full_name": row.get("name", row.get("full_name", "")),
            "emails": [row.get("email", "")] if row.get("email") else [],
            "phones": [normalize_phone(row.get("phone", ""))] if row.get("phone") else [],
            "location": normalize_location(row.get("location", "")),
            "headline": row.get("title", row.get("headline", "")),
            "current_company": row.get("current_company", ""),
            "provenance": [{"field": "all", "source": "recruiter_csv", "method": "direct"}],
            "overall_confidence": 0.9
        }
        return profile