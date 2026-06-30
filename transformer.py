from pathlib import Path
from typing import Dict, Any, List
import json

from sources.base import SourceParser
from sources.recruiter_csv import RecruiterCSVParser
from sources.ats_json import ATSJSONParser
from sources.resume_pdf import ResumePDFParser
from sources.github import GitHubParser
from merger import merge_profiles
from normalizers import normalize_phone, canonical_skill, normalize_location
from config import load_config

class CandidateTransformer:
    def __init__(self):
        self.parsers = {
            'recruiter_csv': RecruiterCSVParser(),
            'ats_json': ATSJSONParser(),
            'resume_pdf': ResumePDFParser(),
            'github': GitHubParser(),
        }
    
    def process_source(self, file_path: Path) -> Dict:
        source_type = SourceParser.detect_type(file_path)
        parser = self.parsers.get(source_type)
        if not parser:
            return {}
        return parser.parse(file_path)
    
    def merge_profiles(self, profiles: List[Dict]) -> Dict:
        return merge_profiles(profiles)
    
    def project(self, canonical: Dict, config: Dict) -> Dict:
        """Runtime configurable output projection."""
        if not config.get("fields"):
            return canonical  # default full schema
        
        result = {}
        for field_spec in config.get("fields", []):
            path = field_spec.get("path")
            from_path = field_spec.get("from", path)
            value = self._get_nested(canonical, from_path)
            
            if field_spec.get("normalize") == "E164":
                value = normalize_phone(value) if isinstance(value, str) else value
            elif field_spec.get("normalize") == "canonical":
                if isinstance(value, list):
                    value = [{"name": canonical_skill(s.get("name", s) if isinstance(s, dict) else s), "confidence": 0.8} for s in value]
            
            result[path] = value
        
        if config.get("include_confidence", True):
            result["overall_confidence"] = canonical.get("overall_confidence", 0.8)
        
        return result
    
    def _get_nested(self, data: Dict, path: str):
        """Simple nested getter (e.g. emails[0])"""
        if '[' in path:
            base = path.split('[')[0]
            idx = int(path.split('[')[1].strip(']'))
            return data.get(base, [])[idx] if isinstance(data.get(base), list) else None
        return data.get(path)