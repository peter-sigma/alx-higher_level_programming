#!/usr/bin/python3
"""Defining a file-appending function."""


def append_write(filename="", text=""):
    """Appending a string to the end of a text file.

    Args:
        filename (str): filename.
        text (str): string to append to the file.
    Returns:
        number of characters append.
    """
    with open(filename, "a", encoding="utf-8") as fl:
        return fl.write(text)
