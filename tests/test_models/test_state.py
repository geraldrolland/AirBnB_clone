"""
This module defines the class TestState
"""

from models.state import State
import json
from models.base_model import BaseModel
import unittest


class TestState(unittest.TestCase):
    """defines the class TestState"""
    def test_state_hasattr_name(self):
        """test state instance for attribute name"""
        state = State()
        self.assertTrue(hasattr(state, "name"))

    def test_state_name(self):
        """test state instance attribute name with value "Lagos" """
        state = State()
        state.name = "Lagos"
        self.assertTrue(state.name, "Lagos")

    def test_state_save(self):
        """test the save() method for serialization"""
        state = State()
        state_id = state.id
        state.save()
        with open("file.json", "r") as file:
            all_obj_dict = json.load(file)
            for obj in all_obj_dict.values():
                if state_id == obj["id"]:
                    self.assertTrue(True)
                continue

    def test_state_basemodel(self):
        """test the state instance for BaseModel class"""
        state = State()
        self.assertTrue(isinstance(state, BaseModel))


if __name__ == "__main__":
    unittest.main()
