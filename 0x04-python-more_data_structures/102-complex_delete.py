#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    _list = list(a_dictionary.keys())
    for v in _list:
        if value == a_dictionary.get(v):
            del a_dictionary[v]

    return (a_dictionary)
