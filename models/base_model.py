#!/usr/bin/python3
"""BaseModel modules for other classes"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """This class defines all common
    attributes/methods for other classes"""

    def __init__(self):
        """Initialize"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the update_at instance attributes with current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        ade_dict = self.__dict__.copy()
        ade_dict['__class__'] = self.__class__.__name__
        ade_dict['created_at'] = self.created_at.isoformat()
        ade_dict['updated_at'] = self.created_at.isoformat()
        return ade_dict
