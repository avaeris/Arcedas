# Contributing to Arcedas

Thank you for your interest in contributing! This guide explains how to set
up a development environment, run tests, and submit high-quality pull
requests.

## Setup

1. Clone the repository:

```bash
git clone git@github.com:avaeris/Arcedas.git
cd Arcedas
```

2. Install dependencies in editable mode so changes to the package are
immediately available to your environment:

```bash
python -m pip install -e .
```

This uses `pyproject.toml` and setuptools to install the package from `src/`.

## Running tests

Run the test suite with pytest:

```bash
python -m pytest -q
```

Tests live in the `tests/` directory and the project uses standard pytest
conventions.

## Branch naming

Use descriptive branches that include the type and short description. Examples:

- `feat/add-foo` — feature work
- `fix/correct-typo` — bug fixes
- `docs/update-readme` — documentation changes

## Pull Request workflow

1. Create a branch from `main`.
2. Make incremental commits with clear messages.
3. Push your branch and open a PR using the template in `.github/`.
4. Ensure tests pass locally and CI is green before requesting review.

## Commit message guidelines

- Use the imperative mood: `Add feature` not `Added feature`.
- Include a short summary line and optional body explaining rationale.
- Include co-author footers for automated or pair contributions where
  appropriate.

Example:

```
Add truncate helper and tests

Co-authored-by: Arcedas-AI <ai@arcedas.local>
```

## Adding new utilities

- Place new Python modules under `src/arcedas/utils/`.
- Add tests in `tests/` and update documentation (README or docs).
- Follow semantic versioning for public API changes and document breaking
  changes in PR descriptions.

## Coding style

- Follow PEP8 for Python code; use 4-space indentation.
- Keep functions small and focused; prefer clear names over clever
  implementations.
- Add docstrings to public helpers and keep them terse and informative.

If you have any questions, open an issue or a draft PR and tag the repo
maintainer.
