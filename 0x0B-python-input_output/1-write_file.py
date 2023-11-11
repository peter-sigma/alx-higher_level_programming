#!/usr/bin/python3
"""Defining a file-writing function."""


def write_file(filename="", text=""):
    """Writting a string to a UTF8 text file.

    Args:
        filename (str): name of the file to write.
        text (str): text to write to the file.
    Returns:
        Number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as fl:
        return fl.write(text)
