"""Simple JSON persistence helper."""

import json
import os
from datetime import datetime
from typing import Any, Dict

def save_state(data: Dict[str, Any], filename: str = "state.json") -> bool:
    """Save data to a JSON file with timestamp."""
    try:
        payload = {
            "saved_at": datetime.now().isoformat(),
            "data": data
        }
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)
        print(f"State saved to {filename}")
        return True
    except Exception as e:
        print(f"Error saving state: {e}")
        return False

def load_state(filename: str = "state.json") -> Dict[str, Any]:
    """Load data from a JSON file."""
    if not os.path.exists(filename):
        print(f"No state file found: {filename}")
        return {}
    try:
        with open(filename, "r", encoding="utf-8") as f:
            payload = json.load(f)
        print(f"State loaded from {filename}")
        return payload.get("data", {})
    except Exception as e:
        print(f"Error loading state: {e}")
        return {}
