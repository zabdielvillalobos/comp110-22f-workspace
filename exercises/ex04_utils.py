"""EX04 List Utility Functions."""

__author__ = "730579449"


def all(numeros: list[int], secret_number: int) -> bool:
    """Returns a bool, True if all numbers matched the indicated number."""
    numeros_index: int = 0 
    if len(numeros) == 0:
        return False
    while numeros_index < len(numeros):
        if numeros[numeros_index] == secret_number:
            numeros_index += 1
        else: 
            return False
    
    return True


def max(super_numeros: list[int]) -> int:
    """Returns LARGEST number in the list."""
    super_numeros_index: int = 1
    numeros_grande: int = 0
    if len(super_numeros) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        if super_numeros[0] > super_numeros[super_numeros_index]:
            numeros_grande = super_numeros[0]
        else:
            numeros_grande = super_numeros[super_numeros_index]
        super_numeros_index += 1
    while super_numeros_index < len(super_numeros):
        if super_numeros[super_numeros_index] > numeros_grande:
            numeros_grande = super_numeros[super_numeros_index]
        else:
            numeros_grande = numeros_grande
        super_numeros_index += 1
    return numeros_grande


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Returns True if every element at every index is equal in both lists."""
    list1_index: int = 0 
    list2_index: int = 0
    if len(list1) != len(list2):
        return False
    while list1_index < len(list1) and list2_index < len(list2):
        if list1[list1_index] == list2[list2_index]:
            list1_index += 1
            list2_index += 1
        else:
            return False
    return True 