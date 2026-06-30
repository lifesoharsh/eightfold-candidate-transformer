import fitz  # PyMuPDF
import re
from pathlib import Path
from typing import Dict, Any
from normalizers import normalize_phone, canonical_skill

class ResumePDFParser:
    def parse(self, file_path: Path) -> Dict[str, Any]:
        if not str(file_path).lower().endswith('.pdf'):
            return {"error": "Not a PDF", "file": str(file_path)}
        
        doc = fitz.open(file_path)
        pages_text = []
        for page in doc:
            pages_text.append(page.get_text())
        text = "".join(pages_text)
        doc.close()
        
        # Extraction
        name_match = re.search(r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})', text.strip())
        email_match = re.search(r'[\w\.-]+@[\w\.-]+', text)
        phone_match = re.search(r'[\+]?[1-9][0-9\s\-\(\)]{8,}', text)
        skills_raw = re.findall(r'(Python|JavaScript|Machine Learning|SQL|AWS)', text, re.I)
        
        profile: Dict[str, Any] = {
            "candidate_id": f"resume_{abs(hash(str(file_path)))}",
            "full_name": name_match.group(1) if name_match else "Unknown Candidate",
            "emails": [email_match.group(0)] if email_match else [],
            "phones": [normalize_phone(phone_match.group(0))] if phone_match else [],
            "skills": [
                {"name": canonical_skill(s), "confidence": 0.8, "sources": ["resume_pdf"]} 
                for s in dict.fromkeys(skills_raw)  # dedup
            ],
            "provenance": [{"field": "all", "source": "resume_pdf", "method": "regex_extract"}],
            "overall_confidence": 0.75
        }
        return profile