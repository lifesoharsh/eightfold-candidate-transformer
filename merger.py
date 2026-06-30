from typing import List, Dict, Any
from thefuzz import fuzz

def merge_profiles(profiles: List[Dict]) -> Dict:
    if not profiles:
        return {}
    
    merged = profiles[0].copy()
    
    for p in profiles[1:]:
        for key, value in p.items():
            if key in ["emails", "phones", "skills", "provenance", "links"]:
                merged.setdefault(key, []).extend(value)
            elif value and (key not in merged or not merged[key] or fuzz.ratio(str(value), str(merged[key])) < 80):
                merged[key] = value  # higher confidence or better match wins
    
    # Dedup skills
    if "skills" in merged:
        seen = {}
        for s in merged["skills"]:
            name = s.get("name", s)
            if name not in seen or s.get("confidence", 0) > seen[name].get("confidence", 0):
                seen[name] = s
        merged["skills"] = list(seen.values())
    
    merged["overall_confidence"] = round(sum(p.get("overall_confidence", 0.5) for p in profiles) / len(profiles), 2)
    return merged