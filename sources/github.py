import requests
from pathlib import Path
from typing import Dict, Any
from .base import SourceParser

class GitHubParser(SourceParser):
    def parse(self, file_path: Path) -> Dict[str, Any]:
        # For demo, assume file_path is URL string or local note
        url = str(file_path)
        if not url.startswith("http"):
            return {"full_name": "GitHub User", "links": [url], "skills": [], "provenance": []}
        
        # Mock GitHub API for demo (real would use token)
        username = url.split("/")[-1]
        profile = {
            "full_name": username.title(),
            "links": [url],
            "headline": f"Engineer at GitHub",
            "skills": [{"name": "Python", "confidence": 0.9, "sources": ["github"]}],
            "provenance": [{"field": "all", "source": "github", "method": "api"}],
            "overall_confidence": 0.8
        }
        return profile