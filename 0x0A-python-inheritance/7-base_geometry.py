#!/usr/bin/python3
"""
Module for class BaseGeometry
"""


class BaseGeometry:
    """A class with public methods area"""
    def area(self):
        """raise exeption"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates if value greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
