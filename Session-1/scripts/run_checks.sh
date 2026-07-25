#!/usr/bin/env bash
set -euo pipefail
python -m pytest -q
python -m src.train --experiment unigram --output-dir results/session_1
