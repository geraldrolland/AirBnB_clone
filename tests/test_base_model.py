#!/usr/bin/python3


"""
This module defines the class Test_BaseModel
"""
import unittest
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """Define the class Test_BaseModel"""
    def test_save(self):
        """This method test the save method for json
        serialization
        """
        my_model = BaseModel()
        my_model.number = 89
        my_model.save()
        self.assertTrue(my_model.updated_at, my_model.created_at)

    def test_to_dict(self):
        """test the to_dict() in the BaseModel for conversion of
        BaseModel object to dict object object for effective serialization
        """
        my_model = BaseModel()
        self.assertTrue(type(my_model.to_dict()), dict)

    def test_kwargs_created_at(self):
        """test the created_key in the keyword argument for string type
        """
        my_model = BaseModel()
        obj_dict = my_model.to_dict()
        self.assertTrue(type(obj_dict["created_at"]), str)

    def test_kwargs_updated_at(self):
        """test the updated_at in keyword argument for string type
        """
        my_model = BaseModel()
        obj_dict = my_model.to_dict()
        self.assertTrue(type(obj_dict["updated_at"]), str)


if __name__ == "__main__":
    unittest.main()
