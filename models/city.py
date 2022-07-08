#!/usr/bin/python3
from models import base_model
"""
City
"""


class City(base_model.BaseModel):
    """
    City class implementing Basemodels
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize method for city
        """
        super().__init__(*args, **kwargs)
