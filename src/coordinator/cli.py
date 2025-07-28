from pathlib import Path

from .state import save_state


def run() -> None:
    save_state({"status": "ok"}, Path("state/run.json"))
