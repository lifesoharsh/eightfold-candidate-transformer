import json
from pathlib import Path
from typing import Dict, Any

def load_config(config_path: Path | None = None) -> Dict[str, Any]:
    if not config_path or not config_path.exists():
        return {
            "fields": [],
            "include_confidence": True,
            "on_missing": "null"
        }
    with open(config_path) as f:
        return json.load(f)