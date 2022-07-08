#!/usr/bin/python3
from models import base_model
"""
State
"""


class State(base_model.BaseModel):
    """
    State class implementing Basemodels
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize method for state
        """
        super().__init__(*args, **kwargs)
