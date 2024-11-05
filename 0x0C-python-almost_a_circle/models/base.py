# !/usr/bin/python3
"""
This module defines the Base class, which serves as the foundational class 
for other classes in this project. The Base class provides a unique ID to 
each instance, either through an explicit ID assignment or via an internal 
auto-incremented counter.

Classes:
    Base - Manages unique identification for instances, serving as the base 
           class for other project classes.
"""


class Base:
    """
    The Base class is the foundational class for managing unique identifiers 
    across derived classes in the project. By keeping track of the number 
    of instances created, it provides a unique ID to each new instance.

    Attributes:
        __nb_objects (int): A private class-level attribute counting the number 
                            of instantiated objects without explicit IDs.
        id (int): The unique identifier for each instance, set explicitly or 
                  assigned based on __nb_objects.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class. If an explicit ID is 
        provided, the instance's id attribute is set to that value. If no 
        ID is provided, the instance's id is automatically set using the 
        __nb_objects counter, which is incremented for each new instance.

        Args:
            id (int, optional): The unique identifier for the instance. 
                                Defaults to None.

        Attributes:
            id (int): The unique identifier for the instance, either passed 
                      explicitly or assigned based on __nb_objects.

        Raises:
            TypeError: If the id provided is not an integer.
        """
        Base.__nb_objects += 1
        if id:
            self.id = id
        else:
            self.id = Base.__nb_objects
