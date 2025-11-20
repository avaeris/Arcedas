from arcedas.utils import normalize_whitespace, truncate, to_title_case


def test_normalize_whitespace_basic():
    assert normalize_whitespace("  a\t b\n  c  ") == "a b c"
    assert normalize_whitespace("single") == "single"


def test_truncate_behaviour():
    assert truncate("hello world", 8) == "hello..."
    assert truncate("short", 10) == "short"
    # when max_length <= len(ellipsis)
    assert truncate("abcdef", 3, ellipsis="...") == "..."[:3]
    assert truncate("", 5) == ""


def test_to_title_case_examples():
    assert to_title_case("hello WORLD") == "Hello World"
    assert to_title_case("  multiple   spaces\tand\nlines") == "Multiple Spaces And Lines"
