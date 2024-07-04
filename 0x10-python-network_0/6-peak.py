#!/usr/bin/python3
"""Implements a peak-finding algorithm."""


def find_peak(list_of_integers):
    """Find and return a peak from a list of unsorted integers."""
    if not list_of_integers:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    mid = size // 2
    if list_of_integers[mid] > list_of_integers[mid - 1] and list_of_integers[mid] > list_of_integers[mid + 1]:
        return list_of_integers[mid]
    elif list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
