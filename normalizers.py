import re
import phonenumbers
from dateutil import parser
from thefuzz import fuzz
from typing import List, Dict, Any

def normalize_phone(phone: str) -> str:
    """Convert to E.164 format."""
    try:
        parsed = phonenumbers.parse(phone, None)
        if phonenumbers.is_valid_number(parsed):
            return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
    except:
        pass
    # Fallback cleanup
    cleaned = re.sub(r'\D', '', phone)
    if len(cleaned) >= 10:
        return f"+1{cleaned[-10:]}"
    return phone

def normalize_date(date_str: str) -> str:
    """Normalize to YYYY-MM."""
    try:
        dt = parser.parse(date_str)
        return dt.strftime("%Y-%m")
    except:
        return date_str
    
def canonical_skill(skill: str) -> str:
    """Simple canonicalization."""
    skill = skill.strip().lower()
    mappings = {
        "javascript": "JavaScript",
        "js": "JavaScript",
        "python": "Python",
        "ml": "Machine Learning",
        "ai": "Artificial Intelligence"
    }
    return mappings.get(skill, skill.title())

def normalize_location(loc_str: str) -> Dict:
    """Basic location parse."""
    # Very simple for demo
    return {"city": loc_str, "region": "", "country": "US"}