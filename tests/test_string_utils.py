from arcedas.utils import slugify


def test_slugify_basic():
    assert slugify("Hello, World!") == "hello-world"


def test_slugify_strips_and_lowercases():
    assert slugify("  Python ROCKS ") == "python-rocks"


def test_slugify_non_string_raises():
    try:
        slugify(None)
    except TypeError:
        assert True
    else:
        assert False, "Expected TypeError for non-string input"
