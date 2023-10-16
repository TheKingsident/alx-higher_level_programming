#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_to_json_string_empty(self):
        data = []
        json_str = Base.to_json_string(data)
        self.assertEqual(json_str, "[]")

    def test_to_json_string_non_empty(self):
        data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        json_str = Base.to_json_string(data)
        self.assertEqual(json_str, '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]')

    def test_save_to_file_rectangle(self):
        r1 = Rectangle(10, 20, 5, 5, 1)
        r2 = Rectangle(5, 10, 1, 1, 2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", 'r') as file:
            content = file.read()
        self.assertEqual(content, '[{"x": 5, "y": 5, "id": 1, "height": 20, "width": 10}, {"x": 1, "y": 1, "id": 2, "height": 10, "width": 5}]')

    def test_save_to_file_square(self):
        s1 = Square(5, 5, 1)
        s2 = Square(10, 2, 2)
        Square.save_to_file([s1, s2])
        with open("Square.json", 'r') as file:
            content = file.read()
        self.assertEqual(content, '[{"id": 1, "size": 5, "x": 5, "y": 1}, {"id": 2, "size": 10, "x": 2, "y": 2}]')

    def test_from_json_string_empty(self):
        json_data = "[]"
        data_list = Base.from_json_string(json_data)
        self.assertEqual(data_list, [])

    def test_from_json_string_non_empty(self):
        json_data = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        data_list = Base.from_json_string(json_data)
        expected = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        self.assertEqual(data_list, expected)

    def test_create_rectangle(self):
        data = {'width': 10, 'height': 20, 'x': 5, 'y': 5, 'id': 1}
        instance = Rectangle.create(**data)
        self.assertEqual(instance.to_dictionary(), data)

    def test_create_square(self):
        data = {'size': 5, 'x': 2, 'y': 2, 'id': 1}
        instance = Square.create(**data)
        self.assertEqual(instance.to_dictionary(), data)

    def test_create_invalid(self):
        data = {'size': 5, 'x': 2, 'y': 2, 'id': 1}
        instance = Base.create(**data)
        self.assertIsNone(instance)

    def test_load_from_file_rectangle(self):
        r1 = Rectangle(10, 20, 5, 5, 1)
        r2 = Rectangle(5, 10, 1, 1, 2)
        Rectangle.save_to_file([r1, r2])
        instances = Rectangle.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertEqual(instances[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(instances[1].to_dictionary(), r2.to_dictionary())

    def test_load_from_file_square(self):
        s1 = Square(5, 5, 1)
        s2 = Square(10, 2, 2)
        Square.save_to_file([s1, s2])
        instances = Square.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertEqual(instances[0].to_dictionary(), s1.to_dictionary())
        self.assertEqual(instances[1].to_dictionary(), s2.to_dictionary())

if __name__ == '__main__':
    unittest.main()
