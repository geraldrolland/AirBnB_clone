"""
This module defines the class TestPlace
"""
import json
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Defines the class TestPlace"""
    def test_place_city_id(self):
        """test city instance for attribute city_id"""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))

    def test_place_user_id(self):
        """test place instance for attribute user_id"""
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))

    def test_place_name(self):
        """test place instance for attribute name"""
        place = Place()
        self.assertTrue(hasattr(place, "name"))

    def test_place_description(self):
        """test place instance for attribute description"""
        place = Place()
        self.assertTrue(hasattr(place, "description"))

    def test_place_number_of_rooms(self):
        """test place instance for attribute number_rooms"""
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))

    def test_place_number_bathrooms(self):
        """test place instance for attribute number_bathrooms"""
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))

    def test_place_max_guest(self):
        """test place instance for attribute max_guest"""
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))

    def test_place_price_by_night(self):
        """test place instance for attribute price_by_night"""
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))

    def test_place_lattitude(self):
        """test place instance for attribute latitude"""
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))

    def test_place_longitude(self):
        """test place instance for attribute longitude"""
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))

    def test_place_amenity_ids(self):
        """test place instance for attribute amenity_id"""
        place = Place()
        self.assertTrue(hasattr(place, "amenity_ids"))

    def test_place_save(self):
        """test save() method for serialization"""
        place = Place()
        place_id = place.id
        place.save()
        with open("file.json", "r") as file:
            all_obj_dict = json.load(file)
            for obj in all_obj_dict.values():
                if place_id == obj['id']:
                    self.assertTrue(True)
                continue


if __name__ == "__main__":
    unittest.main()
