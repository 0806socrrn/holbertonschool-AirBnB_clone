#!/usr/bin/python3

"""
Base models
"""

from datetime import datetime
import uuid


class BaseModel:
    """
    class BaseModel
    """


def __init__(self, **kwargs):
    """
    id: string
    created_at: datetime
    updated_at: datetime
    """
    self.id = str(uuid.uuid4())
    self.updated_at = kwargs.get("updated_at", None)
    self.created_at = kwargs.get("created_at", None)

    current_date = datetime.isoformat(datetime.now())
