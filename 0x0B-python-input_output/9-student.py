#!/usr/bin/python3
"""defining the class Student"""


class Student:
    """ Representation of a student class """

    def __init__(self, first_name, last_name, age):
        """ Initializing the student class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):

        """ returns directory descriping the student instance """
        return self.__dict__.copy()
