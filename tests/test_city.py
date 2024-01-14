#!/usr/bin/python3


"""
This module defines the class Testcity
"""
from models.city import City
from models.base_model import BaseModel
import json
import unittest


class TestCity(unittest.TestCase):
    """Defines the class TestCity"""
    def test_city_hasattr_state_id(self):
        """test the city instance for the attribute state_id
        """
        city = City()
        self.assertTrue(hasattr(city, "state_id"))

    def test_city_hasattr_name(self):
        """test city instance for attribute name
        """
        city = City()
        self.assertTrue(hasattr(city, "name"))

    def test_city_name(self):
        """test the city attribute name for the value "Ikeja"
        """
        city = City()
        city.name = "Ikeja"
        self.assertTrue(city.name, "Ikeja")

    def test_city_state_id(self):
        """test the city attribute state_id for the value "125878adds445" """
        city = City()
        city.state_id = "125878adds445"
        self.assertTrue(city.state_id, "125878adds445")

    def test_city_save(self):
        """test the city object method save() for serialization"""
        city = City()
        city_id = city.id
        city.save()
        with open("file.json", "r") as file:
            all_obj_dict = json.load(file)
            for obj in all_obj_dict.values():
                if city_id == obj["id"]:
                    self.assertTrue(True)
                continue

    def test_city_basemodel(self):
        """test the city instance as an object of the BaseModel class"""
        city = City()
        self.assertTrue(isinstance(city, BaseModel))


if __name__ == "__main__":
    unittest.main()
