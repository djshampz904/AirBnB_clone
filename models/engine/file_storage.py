#!/usr/bin/env python3
"""This module contains the FileStorage class for the AirBnB clone"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """This class serializes instances to a JSON file and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}


    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                new_dict = json.load(f)
                for key, value in new_dict.items():
                    class_name = value['__class__']
                    del value['__class__']
                    self.new(eval(class_name)(**value))
        except FileNotFoundError:
            pass
        except Exception as e:
            raise e

