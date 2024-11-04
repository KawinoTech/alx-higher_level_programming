#!/usr/bin/python3
"""
Module that contains all tests for class Base
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Base()

    def tearDown(self) -> None:
        Base._Base__nb_objects = 0

    def test_id_given(self):
        obj = Base(4)
        self.assertEqual(obj.id, 4)

    def test_id_not_given(self):
        """Test when id is not provided"""
        b2 = Base()
        self.assertEqual(self.obj.id, None)
        self.assertEqual(b2.id, None)

    def test_base_mixed_id(self):
        """Test auto-increment when some instances have ids provided and others do not"""
        b2 = Base()
        b3 = Base()
        self.assertEqual(Base._Base__nb_objects, 3)

if __name__ == '__main__':
    unittest.main()