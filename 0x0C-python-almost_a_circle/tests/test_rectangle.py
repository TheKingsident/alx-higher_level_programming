#!/usr/bin/python3


import unittest
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):

    def test_area(self):
        # Test the area() method
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_display(self):
        # Test the display() method
        rect = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with captured_output() as (out, _):
            rect.display()
        self.assertEqual(out.getvalue(), expected_output)

    def test_str(self):
        # Test the __str__() method
        rect = Rectangle(5, 10, 1, 2, 42)
        expected_output = "[Rectangle] (42) 1/2 - 5/10"
        self.assertEqual(str(rect), expected_output)

    def test_update(self):
        # Test the update() method
        rect = Rectangle(5, 10, 1, 2, 42)
        rect.update(99, width=20, height=30, x=3, y=4)
        self.assertEqual(rect.id, 99)
        self.assertEqual(rect.width, 20)
        self.assertEqual(rect.height, 30)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_to_dictionary(self):
        # Test the to_dictionary() method
        rect = Rectangle(5, 10, 1, 2, 42)
        expected_dict = {'id': 42, 'width': 5, 'height': 10, 'x': 1, 'y': 2}
        self.assertEqual(rect.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
