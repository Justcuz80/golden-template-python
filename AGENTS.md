# AGENTS.md

## Project Purpose
This repository is a reusable Python project template designed to provide a clean,
professional starting point for Python applications.

It includes:
- modern Python packaging
- linting and formatting
- testing structure
- CI automation
- pre-commit hooks

## Repository Structure
src/        → application code
tests/      → unit tests
.github/    → CI workflows

## Development Environment
Python projects should use a virtual environment.

Typical workflow:

make venv
make install

## Code Quality Rules
Follow existing patterns in the repo.

Prefer:
- small focused functions
- readable code
- clear naming
- minimal dependencies

Avoid:
- large refactors unless requested
- breaking existing structure

## Validation Commands
After making changes, run:

make format
make lint
make test
make check

## Done Criteria
A task is complete when:

- code is readable
- tests pass
- linting passes
- changes are minimal and clear
- summary of modifications is provided

## Reporting Changes
When reporting back:

1. summarize what changed
2. list files modified
3. explain why the change improves the project
4. mention validation results
