#!/usr/bin/python3
""" class Square"""


class Square:
    """defines square class"""

    def __init__(self, size=0):
        """initialize square
        Args:
            size: size of the square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size  #: size of the square

    def area(self):
        """returns the area.

        Returns:
            the area
        """
        return self.__size**2
