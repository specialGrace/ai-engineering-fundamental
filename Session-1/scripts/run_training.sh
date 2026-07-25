#!/usr/bin/env bash
set -euo pipefail
EXPERIMENT="${1:-unigram}"
python -m src.train --experiment "$EXPERIMENT" --output-dir "results/session_1_${EXPERIMENT}"
