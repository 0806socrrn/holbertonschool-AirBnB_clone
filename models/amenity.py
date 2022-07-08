#!/usr/bin/python3
from models import base_model
"""
services
"""


class Amenity(base_model.BaseModel):
    """
    implements the Basemodels
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize method
        """
        super().__init__(*args, **kwargs)
