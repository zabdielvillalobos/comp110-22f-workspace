"""Working with dictionaries and their functions for practice."""

__author__ = "730579449"


def invert(invert_dict: dict[str, str]) -> dict[str, str]:
    """Given a dictionary it returns the inverted key and value."""
    user_dict: dict[str, str] = {}
    for x in invert_dict:
        if invert_dict[x] in user_dict:
            raise KeyError
        else: 
            user_dict[invert_dict[x]] = x
    return user_dict


def favorite_color(favorite_dict: dict[str, str]) -> str:
    """Returns the most common color in the dictionary."""
    favorite_dict_color: dict[str, int] = {}
    fav_color: str = ""
    fav_max: int = 0 
    for x in favorite_dict:
        if favorite_dict[x] not in favorite_dict_color:
            favorite_dict_color[favorite_dict[x]] = 0
        favorite_dict_color[favorite_dict[x]] += 1
    for x in favorite_dict_color: 
        if fav_max < favorite_dict_color[x]: 
            fav_max = favorite_dict_color[x]
            fav_color = x
    return fav_color


def count(count_list: list[str]) -> dict[str, int]:
    """Returns a dictionary where each key is a unique value in the given list."""
    dict1: dict[str, int] = {}
    for x in count_list:
        if x in dict1:
            dict1[x] += 1
        else: 
            dict1[x] = 0
            dict1[x] += 1
    return dict1