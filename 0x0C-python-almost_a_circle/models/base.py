#!/usr/bin/python3
"""This is the base class."""


class Base():
    """Definition of class Base."""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


    @classmethod
    def reset_nb_objects(cls):
        """Reset the __nb_objects attribute."""
        cls.__nb_objects = 0

#    @property
#    def id(self):
#        """Function to retrieve the id."""
#        return self.__id
#
#    @id.setter
#    def id(self, value):
#        """This function sets the is when provided."""
#        self.__id = value
