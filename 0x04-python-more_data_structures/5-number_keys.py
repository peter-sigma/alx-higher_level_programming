#!/usr/bin/python3
def number_keys(a_dictionary):
    keys = 0
    _list = list(a_dictionary.keys())

    for i in _list:
        keys += 1

    return (keys)
