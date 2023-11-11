#!/usr/bin/python3
"""Defines an inherited class MyList."""


class MyList(list):
    """uses built in list sorting."""

    def print_sorted(self):
        """Print a list in ascending order."""
        print(sorted(self))
