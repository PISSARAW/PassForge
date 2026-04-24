.PHONY: test test-verbose test-cov

PYTHON ?= .venv/bin/python
TEST ?=

test:
	$(PYTHON) -m pytest $(TEST)

test-verbose:
	$(PYTHON) -m pytest -v

test-cov:
	$(PYTHON) -m pytest --cov=passforge --cov-report=term-missing
