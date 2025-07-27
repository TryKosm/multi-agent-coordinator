import json
from pathlib import Path


def save_state(data: dict[str, object], file: Path) -> None:
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(json.dumps(data, indent=2))
