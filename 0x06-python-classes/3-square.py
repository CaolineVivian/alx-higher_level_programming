#!/usr/bin/python3
# 3-square.py

"""Define a class Square."""


class Square:
    """Represent a square method."""

    def __init__(self, __size=0):
        """check if __size is int"""
        if type(__size) != int:
            raise TypeError("__size must be an integer")
        elif __size < 0:
            raise ValueError("__size must be >= 0")
        self.__size = __size

    def area(self):
        """Return area of the square."""
        return (self.__size * self.__size)
