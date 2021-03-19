#!/usr/bin/python3
# 2-square.py

"""Class that defines a square"""


class Square:

    """checks whether type size is interger or not"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError ("size must be an integer")
        elif size < 0:
            raise ValueError ("size must be >= 0")
