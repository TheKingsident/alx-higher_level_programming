import unittest
from models.square import Square

class TestSquareMethods(unittest.TestCase):

    def test_str(self):
        # Test the __str__() method
        square = Square(5, 2, 3, 42)
        expected_output = "[Square] (42) 2/3 - 5"
        self.assertEqual(str(square), expected_output)

    def test_size_property(self):
        # Test the size property
        square = Square(5)
        self.assertEqual(square.size, 5)
        square.size = 10
        self.assertEqual(square.size, 10)

    def test_update(self):
        # Test the update() method
        square = Square(5, 2, 3, 42)
        square.update(99, size=20, x=4, y=5)
        self.assertEqual(square.id, 99)
        self.assertEqual(square.size, 20)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 5)

    def test_to_dictionary(self):
        # Test the to_dictionary() method
        square = Square(10, 2, 3, 42)
        expected_dict = {'id': 42, 'size': 10, 'x': 2, 'y': 3}
        self.assertEqual(square.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
