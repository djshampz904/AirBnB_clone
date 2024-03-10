#!/usr/bin/python3
"""This module contains the City
class for the AirBnB clone"""
from .base_model import BaseModel


class City(BaseModel):
    """This class inherits from BaseModel and
    defines the attributes of the City class"""
    state_id = ""
    name = ""
