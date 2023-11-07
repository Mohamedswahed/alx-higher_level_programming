#!/usr/bin/python3
""" Defining dictionary with a simple data structure for a JSON"""


def class_to_json(obj):
    """ retuns the dictionary description of an object """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
