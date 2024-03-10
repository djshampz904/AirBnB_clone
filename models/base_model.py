#!/usr/bin/env python3
"""This module contains the BaseModel class for the AirBnB clone"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """This class is the base class for all other classes in this project"""
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self, *args, **kwargs):
        """Initialization of the BaseModel class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    # Instead of this
                    setattr(self,
                            key,
                            datetime.strptime(value,
                                              '%Y-%m-%dT%H:%M:%S.%f'))

                    # Do this
                    setattr(
                        self,
                        key,
                        datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    )
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return the string representation of the BaseModel class"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel class"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
