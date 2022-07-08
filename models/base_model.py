#!/usr/bin/python3
"""
BaseModel class
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """
    BaseModel class defining all common attributes and methods
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
        if kwargs is not None and len(kwargs) != 0:
            for key in kwargs.keys():
                if key != '__class__':
                    setattr(self, key, kwargs[key])
                    if key == "created_at":
                        self.__dict__[key] = datetime.fromisoformat(
                            kwargs[key])
                    if key == "updated_at":
                        self.__dict__[key] = datetime.fromisoformat(
                            kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        return string representation
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """
        time now
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        dictionary of all key and value of instance
        """
        dict_new = self.__dict__.copy()

        dict_new['__class__'] = self.__class__.__name__
        formated_updated = dict_new['updated_at'].isoformat()
        dict_new['updated_at'] = formated_updated
        formated_created = dict_new['created_at'].isoformat()
        dict_new['created_at'] = formated_created
        return (dict_new)
