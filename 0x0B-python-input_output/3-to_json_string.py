#!/usr/bin/python3
""" Defining a function returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """returns JSON representation of an object"""
    return json.dumps(my_obj)
