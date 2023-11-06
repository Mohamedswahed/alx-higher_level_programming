#!/usr/bin/python3
"""
Module for BaseGeometry
"""

class Square(Rectangle):
    """A subclass representing rectangular"""
    def __init__(self, size):
        """constructor of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"method of  area of the square"""
        return self.__size ** 2

    def __str__(self):
        """string reepresenting of the square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
