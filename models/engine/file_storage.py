#!/usr/bin/python3
"""
This module defines the class FileStorage
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review


class FileStorage:
    """Defines tha class FileStorage"""
    __objects = {}
    __file_path = "file.json"

    def all(self):
        """Returns the dictionary __objects"""
        all_object = FileStorage.__objects
        return all_object

    def new(self, obj):
        """Sets in __object to the object of a class
        with key <obj class name>.id
        """
        id = str(obj.id)
        class_name = type(obj).__name__
        id = class_name + "." + id
        FileStorage.__objects[id] = obj

    def save(self):
        """Serializes object using a dictionary data structure to JSON file"""
        all_obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict = {
                key: obj.to_dict()
                }
            all_obj_dict.update(obj_dict)
        with open(FileStorage.__file_path, "w", encoding="UTF8") as file:
            json.dump(all_obj_dict, file)

    def reload(self):
        """Deserialiizes the JSON file to objects only if the JSON file exists.
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="UTF8") as file:
                all_obj_dict = json.load(file)
                for obj_dict in all_obj_dict.values():
                    class_name = obj_dict["__class__"]
                    del obj_dict["__class__"]
                    self.new(eval(class_name)(**obj_dict))
        except FileNotFoundError as e:
            pass
