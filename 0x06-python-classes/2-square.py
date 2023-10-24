#!/usr/bin/python3
"""Square class"""


class Square:
    """defines a square class"""

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
            self.__size = size  #: square size
