#!/usr/bin/python3
"""Class defination."""


class Square:
    """Square representation"""

    def __init__(self, size=0):
        """Square initialization.

        Args:
            size (int): The size of a square.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the size of a square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of a square."""
        return (self.__size * self.__size)
