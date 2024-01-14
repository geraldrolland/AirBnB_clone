#!/usr/bin/python3


"""
This module defines the class Test_FileStorage
"""
from models import storage
from models.base_model import BaseModel
import unittest
import json


class Test_FileStorage(unittest.TestCase):
    """Defines a class Test_FileStorage"""

    def test_all(self):
        """test all() method"""
        my_model = BaseModel()
        my_model.save()
        storage.reload()
        self.assertNotEqual(storage.all(), {})

    def test_new(self):
        """test new() method"""
        my_model = BaseModel()
        my_model.save()
        storage.reload()
        obj_dict = storage.all()
        for obj in obj_dict.values():
            self.assertTrue(isinstance(obj, BaseModel))

    def test_save(self):
        """test the save() method"""
        my_model = BaseModel()
        my_model.save()
        with open("file.json", "r") as file:
            all_obj_dict = file.read()
            self.assertTrue(type(all_obj_dict), str)

    def test_reload(self):
        """test the reload() method"""
        my_model = BaseModel()
        my_model.save()
        with open("file.json", "r") as file:
            all_obj_dict = json.load(file)
            self.assertTrue(type(all_obj_dict), dict)


if __name__ == "__main__":
    unittest.main()

