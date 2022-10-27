"""EX05 - Util Functions."""

__author__ = "730579449"


def only_evens(xs: list[int]) -> list[int]:
    """List returns only even elements."""
    i: int = 0
    return_list: list[int] = list()
    while len(xs) > i:
        if xs[i] % 2 == 0:
            return_list.append(xs[i])
        i += 1
    return return_list


def concat(xs1: list[int], xs2: list[int]) -> list[int]:
    """List returns all elements of xs1 and xs2."""
    i: int = 0 
    i2: int = 0
    list_combined: list[int] = list()
    while i < len(xs1):
        list_combined.append(xs1[i])
        i += 1
    while i2 < len(xs2):
        list_combined.append(xs2[i2])
        i2 += 1
    return list_combined


def sub(xs: list[int], beg: int, end: int) -> list[int]:
    """List of ints generates subset."""
    subset_list: list[int] = list()
    if end > len(xs):
        end = len(xs)
    if beg < 0:
        beg = 0
    if beg > len(xs):
        return []
    if end <= 0:
        return []
    while beg < end:
        subset_list.append(xs[beg])
        beg += 1
    return subset_list