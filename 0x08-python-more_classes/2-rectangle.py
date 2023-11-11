#!/usr/bin/python3
"""Defination of a Rectangle class."""


class Rectangle:
    """Representation of a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializing a new rectangle.

        Args:
            width (int): width of our new rectangle.
            height (int): height of our new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """A function that return the area of our rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """A function that return the perimeter of our rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
