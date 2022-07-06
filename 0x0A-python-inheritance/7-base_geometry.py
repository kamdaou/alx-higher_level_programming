#!/usr/bin/python3
class BaseGeometry:
    """
    BaseGeometry class
    Methods:
        area: raises an Exception with the message area() is not implemented
        integer_validator: validates values
    """
    def area(self):
        """
        raises an Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates values
        Args:
            name: name of the variable
            value: value of the variable
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
