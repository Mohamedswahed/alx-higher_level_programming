#!/usr/bin/python3
"""defines a function that adds attribute to an object
"""


def add_attribute(obj, attribute, value):
    """dds a new attribute"""
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    if '__slots__' in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attribute, value)
