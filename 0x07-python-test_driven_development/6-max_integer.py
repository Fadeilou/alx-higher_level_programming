#!/usr/bin/python3
"""Module to find the max integer in a list
"""

def max_integer(lst=None):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if lst is None:
        return None
    if not isinstance(lst, list):
        raise TypeError("list must be a list")
    if len(lst) == 0:
        return None
    result = lst[0]
    for num in lst[1:]:
        if num > result:
            result = num
    return result
