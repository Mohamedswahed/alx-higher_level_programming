#!/usr/bin/python3
"""
class MyInt
"""


class MyInt(int):
    """rebel version of an integer class"""
    def __new__(cls, *args, **kwargs):
        """create instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """ != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """ == is now !="""
        return int(self) == other
