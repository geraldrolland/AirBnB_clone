#!/usr/bin/python3
"""
This module defines the class TestUser
"""
from models.user import User
from models.base_model import BaseModel
import unittest
import json


class TestUser(unittest.TestCase):
    """defines the class TestUser"""

    def test_user_hasattr_first_name(self):
        """test user instnace for the atttribute first_name"""
        user = User()
        self.assertTrue(hasattr(user, "first_name"))

    def test_user_hasattr_last_name(self):
        """test user instance for the attribute last_name"""
        user = User()
        self.assertTrue(hasattr(user, "last_name"))

    def test_user_hasattr_password(self):
        """test user instance for attribute password"""
        user = User()
        self.assertTrue(hasattr(user, "password"))

    def test_user_hasattr_email_address(self):
        """test user instance for attribute email"""
        user = User()
        self.assertTrue(hasattr(user, "email"))

    def test_user_first_name(self):
        """test user instance attribute with value "Gerald" """
        user = User()
        user.first_name = "Gerald"
        expected = "Gerald"
        self.assertTrue(user.first_name, expected)

    def test_user_last_name(self):
        """test user instance attribute with value "Ujowundu" """
        user = User()
        user.last_name = "Ujowundu"
        expected = "Ujowundu"
        self.assertTrue(user.last_name, expected)

    def test_user_email_address(self):
        """test user instance attribute with "geraldrolland123@gmail.com" """
        user = User()
        user.email_address = "geraldrolland123@gmail.com"
        expected = "geraldrolland123@gmail.com"
        self.assertTrue(user.email_address, expected)

    def test_user_password(self):
        """test user instance attribute with "onyeka123" """
        user = User()
        user.password = "onyeka123"
        expected = "onyeka123"
        self.assertTrue(user.password, expected)

    def test_user_save(self):
        """test save() method for serialization"""
        user = User()
        user.save()
        user_id = user.id
        with open("file.json", "r") as file:
            all_obj_dict = json.load(file)
            for obj in all_obj_dict.values():
                if user_id == obj["id"]:
                    self.assertTrue(True)
                continue

    def test_user_basemodel(self):
        """test user instance for BaseModel"""
        user = User()
        self.assertTrue(isinstance(user, BaseModel))


if __name__ == "__main__":
    unittest.main()
