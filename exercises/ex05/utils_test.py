""" EX05."""

__author__ = "730579449"


"""Tests for the sum function."""


from utils import only_evens, concat, sub


def test_only_evens_empty() -> None:
    xs: list[int] = []
    assert only_evens([]) == []


def test_only_evens_single_item() -> None:
    xs: list[int] = [4]
    assert only_evens(xs) == [4]


def test_only_evens_many_items() -> None:
    xs: list[int] = [4, 4, 4]
    assert only_evens(xs) == [4, 4, 4]


    def test_concat_empty() -> None:
    xs: list[int] = []
    assert concat([]) == 0.0


def test_concat_single_item() -> None:
    xs: list[int] = [110.0]
    assert concat(xs) == 110.0


def test_concat_many_items() -> None:
    xs: list[float] = [1.0, 2.0, 3.0]
    assert concat(xs) == 6.0


def test_sub_empty() -> None:
    xs: list[float] = []
    assert sub([]) == 0.0


def test_sub_single_item() -> None:
    xs: list[float] = [110.0]
    assert sub(xs) == 110.0


def test_sub_many_items() -> None:
    xs: list[float] = [1.0, 2.0, 3.0]
    assert sub(xs) == 6.0


