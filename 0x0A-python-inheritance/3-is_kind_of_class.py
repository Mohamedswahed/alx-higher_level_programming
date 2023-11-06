#!/usr/bin/python3
"""
module for is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """Detrmine if the object is subclass from a_class, else False"""
    return (isinstance(obj, a_class))
