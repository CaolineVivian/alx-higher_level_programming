#!/usr/bin/python3
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
        self.__size = size
        if type(size) != int:
            raise TypeError ("size must be an integer")
        elif size < 0:
            raise ValueError ("size must be >= 0")

    def area(self):
        """
        public instance method that returns current square area
        """
        return (self.size * self.size)
