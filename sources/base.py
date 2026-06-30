from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, Any

class SourceParser(ABC):
    @abstractmethod
    def parse(self, file_path: Path) -> Dict[str, Any]:
        pass

    @staticmethod
    def detect_type(file_path: Path) -> str:
        suffix = file_path.suffix.lower()
        if suffix == '.csv':
            return 'recruiter_csv'
        elif suffix == '.json':
            return 'ats_json'
        elif suffix == '.pdf':
            return 'resume_pdf'
        elif 'github' in str(file_path).lower() or file_path.suffix == '':
            return 'github'
        return 'unknown'