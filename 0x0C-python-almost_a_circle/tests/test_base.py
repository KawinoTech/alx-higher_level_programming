# !/usr/bin/python3
"""
This module contains unit tests for the Base class, which is the base class 
for managing unique identifiers within a hierarchy of shapes or geometric objects. 
The tests ensure that the Base class behaves as expected when handling IDs, 
whether provided explicitly or auto-assigned.

Classes:
    TestBase - A test case class derived from unittest.TestCase, containing 
               various unit tests for verifying the functionality of the Base class.
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    TestBase class conducts a suite of unit tests to verify the functionality 
    of the Base class. It checks that instances are assigned unique identifiers,
    either by explicit assignment or by an internal auto-increment mechanism.

    Methods:
        setUp() - Initializes a test case with a Base instance.
        tearDown() - Resets the class-level counter for unique identifiers.
        test_id_given() - Verifies that an explicitly given ID is assigned correctly.
        test_id_not_given() - Verifies that an ID is correctly set to None when not provided.
        test_base_mixed_id() - Ensures correct handling of mixed explicit and auto-generated IDs.
    """

    def setUp(self) -> None:
        """
        Set up method runs before each test. It initializes a Base instance for use
        within each test case, ensuring a fresh state.

        Attributes:
            obj (Base): A new instance of the Base class for testing.
        """
        self.obj = Base()

    def tearDown(self) -> None:
        """
        Tear down method runs after each test. It resets the class-level counter,
        _Base__nb_objects, to 0 to ensure that ID auto-incrementing starts fresh 
        for each test case. This prevents test cases from affecting one another.
        """
        Base._Base__nb_objects = 0

    def test_id_given(self):
        """
        Test case for explicitly given ID. Verifies that when an ID is passed 
        to the Base constructor, the instance's id attribute correctly reflects 
        the given ID.
        """
        obj = Base(4)
        self.assertEqual(obj.id, 4)

    def test_id_not_given(self):
        """
        Test case for auto-assigned ID. Verifies that when no ID is provided, 
        the instance's id attribute is set to None.

        Creates a second Base instance to ensure default behavior is consistent.
        """
        b2 = Base()
        self.assertEqual(self.obj.id, None)
        self.assertEqual(b2.id, None)

    def test_base_mixed_id(self):
        """
        Test case for mixed explicit and implicit ID assignment. This test checks 
        that the Base class correctly handles a mix of instances with and without 
        explicitly provided IDs.

        It verifies that the internal counter, _Base__nb_objects, accurately reflects 
        the number of instances created without explicit IDs, accounting for automatic ID increments.
        """
        b2 = Base()
        b3 = Base()
        self.assertEqual(Base._Base__nb_objects, 3)


if __name__ == '__main__':
    unittest.main()
