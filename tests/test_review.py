#!/usr/bin/python3


"""
This module defines the class TestReview
"""
import json
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Defines the class TestReview"""

    def test_review_place_id(self):
        """test review instance attribute place_id"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))

    def test_review_user_id(self):
        """test review instance attribute user_id"""
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))

    def test_review_text(self):
        """test review instance attribute text"""
        review = Review()
        self.assertTrue(hasattr(review, "text"))

    def test_review_save(self):
        """test save() method for serialization"""
        review = Review()
        review_id = review.id
        review.save()
        with open("file.json", "r") as file:
            all_obj_dict = json.load(file)
            for obj in all_obj_dict.values():
                if review_id == obj["id"]:
                    self.assertTrue(True)
                continue


if __name__ == "__main__":
    unittest.main()
