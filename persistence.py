# persistence.py
# Simple JSON-based persistence for saving/loading application state.

import json
import os
from datetime import datetime


from typing import Any


def save_state(data: dict[str, Any], filename: str) -> bool:
    """
    Save data to a JSON file.

    Args:
        data: Dictionary to save
        filename: Path to save file

    Returns:
        True if successful, False otherwise
    """
    try:
        save_data: dict[str, Any] = {
            "version": "1.0",
            "saved_at": datetime.now().isoformat(),
            "data": data,
        }

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(save_data, f, indent=2, default=str)

        print(f"[SAVED]: {filename}")
        return True

    except (IOError, TypeError) as e:
        print(f"[ERROR]: Failed to save - {e}")
        return False


def load_state(filename: str) -> dict[str, Any]:
    """
    Load data from a JSON file.

    Args:
        filename: Path to the JSON file

    Returns:
        Dictionary with loaded data, or empty dict if load fails
    """
    if not os.path.exists(filename):
        print(f"[INFO]: No saved state found at '{filename}'")
        return {}

    try:
        with open(filename, "r", encoding="utf-8") as f:
            save_data = json.load(f)

        # Handle both raw data and wrapped format
        if "data" in save_data:
            print(
                f"[LOADED]: {filename} (saved {save_data.get('saved_at', 'unknown')})"
            )
            return save_data["data"]
        else:
            return save_data

    except json.JSONDecodeError as e:
        print(f"[ERROR]: Invalid JSON - {e}")
        return {}
    except IOError as e:
        print(f"[ERROR]: Failed to read - {e}")
        return {}
