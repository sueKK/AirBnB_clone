#!/usr/bin/python3
"""

"""
import uuid
from datetime import datetime


class BaseModel:

    def _init_(self, *args, **kwargs):
        time_formart = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key. value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_a" or key == "updated_at":
                    setattr(self. key. datetime.strptime(value. time_format))
                else:
                    setattr(self. key. value)
        else:
            self.id = str(uuid.uuid4())

            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the instance to a dictionary.

        """
        result_dict = self._dict_.copy()
        result_dict['_class'] = self.__class.__name_
        result_dict['created_at'] = self.created_at.isoformat()
        result_dict['updated_at'] = self.updated_at.isoformat()
        return result_dict

    def _str_(self):
        """
        Returns a string representation of the instance.

        """
        return "[{}] ({}) {}".format(
            self._class.__name, self.id, self.__dict_
        )
