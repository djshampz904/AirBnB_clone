#!/usr/bin/env python3
"""This module contains the User class for the AirBnB clone"""
from .base_model import BaseModel


class User(BaseModel):
    """This class inherits from BaseModel and
    defines the attributes of the User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of the User class"""
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', "")
        self.password = kwargs.get('password', "")
        self.first_name = kwargs.get('first_name', "")
        self.last_name = kwargs.get('last_name', "")
