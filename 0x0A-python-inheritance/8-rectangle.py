#!/usr/bin/python3
"""
Module for class BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A subclass of a rectangle"""
    def __init__(self, width, height):
        """Construcotrs of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
