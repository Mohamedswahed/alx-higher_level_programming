#!/usr/bin/python3
"""
module for is_same_class
"""


def is_same_class(obj, a_class):
    """return true if obj is the exact class a_class"""
    return (type(obj) == a_class)
