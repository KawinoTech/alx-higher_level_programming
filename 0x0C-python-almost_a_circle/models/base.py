#!/usr/bin/python3
"""
Module containing Base class
Base class will be the “base” of all other classes in this project
"""


class Base:
    """
    Class Base

    Attrs:
        private class __nb_objects: no. of objects instantiated and current
        public instance id: id of instance
    """
    __nb_objects = 0

    def __init__(self, id=None):
        Base.__nb_objects += 1
        if id:
            self.id = id
        else:
            self.id = Base.__nb_objects
