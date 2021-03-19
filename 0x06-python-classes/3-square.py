#!/usr/bin/python3
# 3-square.py
"""
  class that defines a square
"""
class Square:
    """
        method that define the class
    """
    def __init__(self, size=0):
        """
        checks for integers
        """
        self.__size = __size
        if type(size) != int:
            raise TypeError ("__size must be an integer")
        elif size < 0:
            raise ValueError ("__size must be >= 0")

    def area(self):
        """
        public instance method that returns current square area
        """
        return (self.__size * self.__size)
