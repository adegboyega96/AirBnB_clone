#!/usr/bin/python3
"""BaseModel modules for other classes"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """This class defines all common
    attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize"""
        if kwargs is not None and len(kwargs) != 0:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]

        else:
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
