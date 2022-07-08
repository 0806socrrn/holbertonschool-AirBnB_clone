#!/usr/bin/python3
from models import base_model
"""
User
"""


class User(base_model.BaseModel):
    """
    User class implementing Basemodels
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize method for user
        """
        super().__init__(*args, **kwargs)
