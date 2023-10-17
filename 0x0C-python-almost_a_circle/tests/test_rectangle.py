#!/usr/bin/python3


import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestRectangleMethods(unittest.TestCase):

    def test_area(self):
        # Test the area() method
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_str(self):
        # Test the __str__() method
        rect = Rectangle(5, 10, 1, 2, 42)
        expected_output = "[Rectangle] (42) 1/2 - 5/10"
        self.assertEqual(str(rect), expected_output)


    def test_update_only_id(self):
        # Test updating only the ID
        square = Square(5, 2, 3, 42)
        square.update(99)
        self.assertEqual(square.id, 99)
        self.assertEqual(square.size, 5)  # Size should remain unchanged
        self.assertEqual(square.x, 2)  # x should remain unchanged
        self.assertEqual(square.y, 3)

    def test_to_dictionary(self):
        # Test the to_dictionary() method
        rect = Rectangle(5, 10, 1, 2, 42)
        expected_dict = {'id': 42, 'width': 5, 'height': 10, 'x': 1, 'y': 2}
        self.assertEqual(rect.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
