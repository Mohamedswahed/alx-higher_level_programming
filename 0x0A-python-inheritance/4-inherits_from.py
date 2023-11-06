#!/usr/bin/python3
"""
module for inherits_from method
"""


def inherits_from(obj, a_class):
    """Detrmine if the object  subclass of a_class"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
