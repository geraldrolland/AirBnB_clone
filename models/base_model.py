#!/usr/bin/python3
"""
This module defines the class BasModel
"""
import models
import uuid
import datetime


class BaseModel:
    """Defines the class BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initializes the attribute of the object.
        args:
            args(tuple): A tuple containing the attribute of the objects
            kwargs(dict): A dictionary containing the attribute of the objects
        """
        if kwargs != {}:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = kwargs[key]
                    value = datetime.datetime.fromisoformat(value)
                setattr(self, key, value)
            return
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        models.storage.new(self)

    def __str__(self):
        """Return the string represantation of the class object"""
        class_name = type(self).__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing
        all keys/values of __dict__ of the instance
        """
        obj_dict = self.__dict__.copy()
        class_name = type(self).__name__
        obj_dict.update({"__class__": class_name})
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.created_at.isoformat()
        return obj_dict
