#!/usr/bin/python3
"""
Module containing Model MyList that inherits
from class 'list'
"""


class MyList(list):
    """
    A MyList class, sub-class of primitive data-type list
    methods: printed_sorted
    """

    def print_sorted(self):
        """
        Pubic instance method that prints the list1,
        but sorted (ascending sort)
        """
        list1 = self[:]
        list1.sort()
        print(list)
