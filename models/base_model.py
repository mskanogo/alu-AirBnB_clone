#!/usr/bin/python3
"""This module defines the BaseModel class.

BaseModel is the parent class for all AirBnB models. It handles
initialization, serialization, and deserialization of instances.
"""
import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes and methods for other AirBnB classes.

    Every model in this project inherits from BaseModel to receive a
    unique id, creation timestamp, update timestamp, and the ability
    to serialize/deserialize itself.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.

        There are two ways to create a BaseModel:
        1. Brand new: BaseModel() - generates a fresh id and timestamps,
           then registers itself with storage so it can be saved.
        2. From a dict: BaseModel(**some_dict) - rebuilds a saved instance.
           We do NOT call storage.new() here because the object already
           exists in storage (we are just recreating it in memory).

        Args:
            *args: Not used. Kept for compatibility.
            **kwargs: Key/value pairs to rebuild an instance from a dict.
                      '__class__' key is ignored (not set as attribute).
                      'created_at' and 'updated_at' are converted from
                      ISO format strings back to datetime objects.
        """
        if kwargs:
            # Rebuilding from a saved dictionary
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"
                    )
                setattr(self, key, value)
        else:
            # Brand new instance
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # Tell storage this object exists so it will be saved
            from models import storage
            storage.new(self)

    def __str__(self):
        """Return a readable string representation of the instance.

        Format: [ClassName] (id) {attribute dictionary}
        """
        return "[{}] ({}) {}".format(
            type(self).__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """Update 'updated_at' to now and persist all objects to the file."""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance.

        Includes all instance attributes plus '__class__', and converts
        both datetime fields to ISO 8601 strings for JSON compatibility.

        Returns:
            dict: A serializable snapshot of this instance.
        """
        result = self.__dict__.copy()
        result["__class__"] = type(self).__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result