"""EX05 - Testing Util Functions."""

__author__ = "730579449"


from utils import only_evens, concat, sub


def test_only_evens_empty() -> None:
    """Returns empty list."""
    xs: list[int] = list()
    assert only_evens(xs) == []


def test_only_evens_single_item() -> None:
    """Return only evens."""
    xs: list[int] = [1, 2, 3, 4]
    assert only_evens(xs) == [2, 4]


def test_only_evens_many_items() -> None:
    """Checks for negatives."""
    xs: list[int] = [-4, 4, 4]
    assert only_evens(xs) == [-4, 4, 4]


def test_concat_edge_case() -> None:
    """Return an empty string."""
    xs1: list[int] = list()
    xs2: list[int] = list()
    assert concat(xs1, xs2) == []


def test_concat_different_lengths() -> None:
    """Checks for differing lengths."""
    xs1: list[int] = [4, 6, 8, 7]
    xs2: list[int] = [1, 2, 3]
    assert concat(xs1, xs2) == []


def test_concat_many_items() -> None:
    """Checks for general functionality."""
    xs1: list[int] = [1, 2, 3]
    xs2: list[int] = [4, 5, 6]
    assert concat(xs1, xs2) == [1, 2, 3, 4, 5, 6]


def test_sub_empty() -> None:
    """Returns empty list."""
    xs: list[int] = []
    assert sub(xs, 10, -2) == []


def test_sub_many_items() -> None:
    """Tests sub works."""
    xs: list[int] = [10, 25, 42, 67, 96]
    assert sub(xs, 1, 3) == [25, 42]


def test_sub_negative_beg() -> None:
    """Negative work test."""
    xs: list[int] = [1, 2, 3, 4, 5]
    assert sub(xs, -1, 3) == [1, 2, 3]