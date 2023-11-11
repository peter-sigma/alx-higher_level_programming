#!/usr/bin/python3
"""Defination of class square"""


class Square:
    """square representation"""

    def __init__(self, size=0):
        """Square initialization.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
