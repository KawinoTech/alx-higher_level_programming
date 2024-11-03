#!/usr/bin/python3
"""
Module containing function look_up
"""
class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

def lookup(obj):
    """
    Function that returns the list of available
    attributes and methods of an object

    Args:
        obj:  Object source
    """
    return dir(obj)

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))