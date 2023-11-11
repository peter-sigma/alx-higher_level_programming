#!/usr/bin/python3
"""Defining inherited list MyList."""


class MyList(list):
    """Implementing built-in sort"""

    def print_sorted(self):
        """Print list in ascending order"""
        print(sorted(self))
