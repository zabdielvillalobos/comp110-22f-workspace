"""EX07 Dictionaries Tests."""

__author__ = "730579449"


import pytest
from dictionary import invert, favorite_color, count


def test_invert_items() -> None:
    """Tests to see if the dict is not empty."""
    dict1: dict[str, str] = {'1': '2', '3': '4'}
    assert invert(dict1) == {'2': '1', '4': '3'}


def test_invert_empty() -> None: 
    """Checks to see if the invert dict is empty."""
    dict1: dict[str, str] = {}
    assert invert(dict1) == {}


def test_error_invert() -> None: 
    """Checks to see if the raise key error works."""
    with pytest.raises(KeyError):
        dict1 = {'zab': 'villalobos', 'karim': 'benzema'}
        invert(dict1)


def test_favorite_items() -> None:
    """Tests to see if the dict is not empty."""
    dict1: dict[str, str] = {"Zab": "Red", "Daniel": "Blue", "Joshy": "Red"}
    assert favorite_color(dict1) == "Red"


def test_favorite_tie() -> None:
    """Tests to see if the dict is a tie."""
    dict1: dict[str, str] = {"Zab": "Red", "Daniel": "Blue", "Joshy": "Red", "Lucas": "Blue"}
    assert favorite_color(dict1) == "Red"


def test_favorite_empty() -> None: 
    """Checks to see if the favorite dict is empty."""
    dict1: dict[str, str] = {}
    assert favorite_color(dict1) == ""


def test_count_empty() -> None: 
    """Checks to see if the count list is empty."""
    list1: list[str] = []
    assert count(list1) == {}


def test_count_single() -> None: 
    """Checks for single item in dict."""
    list1: list[str] = ['1', '1', '1', '1']
    assert count(list1) == {'1': 4}


def test_count_many() -> None: 
    """Checks to see for many items in dict."""
    list1: list[str] = ['1', '1', '2', '3', '3', '4', '4', '4']
    assert count(list1) == {'1': 2, '2': 1, '3': 2, '4': 3}
