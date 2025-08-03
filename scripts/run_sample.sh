#!/usr/bin/env bash
set -euo pipefail
python - <<'PY'
from coordinator import run
run()
print("wrote state/run.json")
PY
