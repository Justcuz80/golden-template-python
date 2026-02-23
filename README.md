# golden-template-python

Reusable professional Python project template:
- `src/` layout
- Ruff linting + formatting
- Pytest
- Pre-commit hooks
- Makefile commands for repeatable workflow

## Setup

```bash
make venv
source .venv/bin/activate
make install
pre-commit install
```

## Common commands

```bash
make format   # auto-fix + format
make lint     # check only
make test
make check    # lint + test
```
