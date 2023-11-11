#!/usr/bin/python3
""" Find the Peak values """


def find_peak(list_of_integers):
    list_length = len(list_of_integers)
    """ return None if the list is empty """
    if list_length == 0:
        return None
    start, end = 0, list_length - 1
    mylist = list_of_integers
    while start < end:
        mid = start + (end - start) // 2
        if mylist[mid] > mylist[mid - 1] and mylist[mid] > mylist[mid + 1]:
            return mylist[mid]
        if mylist[mid - 1] > mylist[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return mylist[start]
