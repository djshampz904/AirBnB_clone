#!/usr/bin/python3
"""This module contains the Review class for the AirBnB clone"""
from .base_model import BaseModel


class Review(BaseModel):
    """This class inherits from BaseModel and
    defines the attributes of the Review class"""
    place_id = ""
    user_id = ""
    text = ""
