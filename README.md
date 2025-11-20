# Arcedas

A small utility library and starter project for Arcedas — focused on simple
helpers, tests, and CI to bootstrap development.

## Features

- Small string utility helpers (slugify, sanitize)
- Pytest-based tests
- GitHub Actions CI for running tests

## Additional Helpers

This project includes a few additional string helper utilities in
`arcedas.utils`:

- `truncate(text, max_length)`: Safely shorten long text and append an ellipsis when truncated.
- `normalize_whitespace(text)`: Collapse multiple spaces, tabs, and newlines into single spaces and strip leading/trailing whitespace.
- `to_title_case(text)`: Convert text into human-friendly title case while normalizing whitespace.

These helpers are small, well-tested, and useful across text-processing tasks.

## Getting started

Clone the repo and run tests locally:

```bash
git clone git@github.com:avaeris/Arcedas.git
cd Arcedas
# Install in editable mode so the package is available to tests
python -m pip install -e .
python -m pytest -q
```

## Contributing

Contributions are welcome. Create a branch for each improvement and open a
pull request describing what changed and why.

Co-authored commits are supported; the automation agent may add a co-author
footnote for changes made programmatically.

## License

MIT