#!/usr/bin/python3
# 2-square.py

"""
  class that defines a square
"""


class Square:
    """
        method that define the class
    """
    def __init__(self, size=0):
        """checks whether type size is interger or not"""
        self.__size = size
        if type(size) != int:
            raise TypeError ("size must be an integer")
        elif size < 0:
            raise ValueError ("size must be >= 0")
