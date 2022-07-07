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


def __init__(self, *args, **kwargs):
    """
    id: string
    created_at: datetime
    updated_at: datetime
    """


self.id = str(uuid.uuid4())
self.created_at = datetime.now()
self.updated_at = datetime.now()
models.storage.new(self)


def save(self):
    """
    updated to the current date
    """
    self.updated_at = datetime.now()
    models.storage.save()

    def dict(self):
        """Returns a dictionary"""
    dictionary = self.__dict__.copy()
    dictionary['__class__'] = self.__class__.__name__
    dictionary['created_at'] = self.created_at.isoformat()
    dictionary['updated_at'] = self.updated_at.isoformat()
    return dictionary
