"""Load bundled datasets and validate basic provenance/schema invariants."""
import json
from pathlib import Path
_DIR=Path(__file__).with_name("data")
def _load(name):
    with (_DIR/name).open(encoding="utf-8") as f: return json.load(f)
def load_reference_dataset():
    data=_load("reference_elements.json")
    if not data.get("metadata",{}).get("sources") or not data.get("elements"): raise ValueError("missing provenance or elements")
    for symbol,item in data["elements"].items():
        if not symbol[0].isupper() or not item.get("name") or not isinstance(item.get("atomic_weight"),(int,float)) or item["atomic_weight"]<=0:
            raise ValueError(f"invalid element entry: {symbol}")
    return data
def load_natural_process_dataset():
    data=_load("natural_processes.json")
    if not data.get("metadata",{}).get("not_for_prediction"): raise ValueError("illustrative parameters must be marked not_for_prediction")
    return data
