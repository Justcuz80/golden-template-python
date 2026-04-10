# Golden Template Python

A professional Python CLI project template designed for automation tools, bots, and command-line utilities.

This template provides a clean structure, modern tooling, and a repeatable developer workflow so new projects can start quickly without rebuilding infrastructure.

---

# Features

This template includes:

* Python **src layout**
* Installable package via `pyproject.toml`
* CLI entrypoint (`golden-template`)
* Argument parsing with `argparse`
* Environment-based configuration
* `.env` support
* Structured logging
* Automated tests with `pytest`
* Linting and formatting with `ruff`
* Pre-commit hooks
* Makefile developer workflow
* One-command project bootstrap
* AI coding agent guidance (`AGENTS.md`)

---

# Project Structure

```
src/
 └─ app/
     ├─ cli.py
     ├─ config.py
     ├─ logging_config.py
     └─ hello.py

tests/
 ├─ test_cli.py
 ├─ test_config.py
 └─ test_hello.py
```

Execution flow:

```
CLI
 ↓
config + CLI args
 ↓
application logic
 ↓
logging
 ↓
tests
```

---

# Quick Start

Clone the repository and bootstrap the environment.

```bash
git clone <repo-url>
cd golden-template-python
make bootstrap
```

This command will:

* create a virtual environment
* install dependencies
* install pre-commit hooks

---

# Run the Application

```
make run
```

or directly:

```
golden-template
```

Example with arguments:

```
golden-template --name David
```

---

# Environment Configuration

Configuration can be provided through environment variables or a `.env` file.

Example `.env`:

```
APP_DEFAULT_NAME=Justin
APP_LOG_LEVEL=INFO
APP_ENV=development
```

Override at runtime:

```
APP_DEFAULT_NAME=Marcus golden-template
```

---

# Developer Workflow

Run tests:

```
make test
```

Run lint checks:

```
make lint
```

Format code automatically:

```
make format
```

Run full validation:

```
make check
```

Clean caches:

```
make clean
```

---

# Creating a New Project from This Template

Typical workflow:

```
git clone <template>
cd new-project
make bootstrap
make run
```

Then begin building your application logic inside:

```
src/app/
```

---

# Philosophy

This template prioritizes:

* **CLI automation tools**
* strong project structure
* reproducible environments
* automated quality checks
* minimal boilerplate

It is intended for tools such as:

* automation scripts
* trading bots
* scanners
* file processors
* internal developer tools

---

# License

MIT
