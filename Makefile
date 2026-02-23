.PHONY: help venv install format lint test check run clean

help:
	@echo "make venv      - create virtual environment"
	@echo "make install   - install dev dependencies"
	@echo "make format    - auto-format and fix lint issues"
	@echo "make lint      - run lint checks (no changes)"
	@echo "make test      - run tests"
	@echo "make check     - lint + test"
	@echo "make clean     - remove caches"

venv:
	python3 -m venv .venv

install:
	. .venv/bin/activate && pip install -U pip && pip install ruff pytest pre-commit

format:
	ruff check . --fix
	ruff format .

lint:
	ruff check .
	ruff format . --check

test:
	pytest

check: lint test

clean:
	rm -rf .pytest_cache .ruff_cache __pycache__ .coverage .mypy_cache
	find . -type d -name "__pycache__" -prune -exec rm -rf {} \; 2>/dev/null || true
