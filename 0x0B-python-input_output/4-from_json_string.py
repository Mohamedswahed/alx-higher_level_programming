#!/usr/bin/python3
""" Defining a function that returns an object from
a JSON representation
"""
import json


def from_json_string(my_str):
    """ Returns an object by a JSON """
    return json.loads(my_str)
