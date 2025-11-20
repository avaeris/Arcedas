"""String helper utilities.

This module contains a small set of deterministic string helpers used in
examples and tests.
"""
import re


def slugify(value: str) -> str:
    """Return a URL-friendly slug for `value`.

    Examples:
        >>> slugify('Hello, World!')
        'hello-world'
    """
    if not isinstance(value, str):
        raise TypeError("value must be a string")
    value = value.strip().lower()
    # replace any sequence of non-alphanumeric characters with a single hyphen
    value = re.sub(r"[^a-z0-9]+", "-", value)
    # strip leading/trailing hyphens
    return value.strip("-")
