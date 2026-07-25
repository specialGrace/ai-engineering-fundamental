PYTHON ?= python
VENV ?= .venv

.PHONY: setup notebook test train train-bigram check clean

setup:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/python -m pip install --upgrade pip
	$(VENV)/bin/python -m pip install -r requirements.txt

notebook:
	$(PYTHON) -m jupyter lab

test:
	$(PYTHON) -m pytest -q

train:
	$(PYTHON) -m src.train --experiment unigram

train-bigram:
	$(PYTHON) -m src.train --experiment bigram --output-dir results/session_1_bigram

check: test train

clean:
	rm -rf results/session_1 results/session_1_bigram .pytest_cache
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
