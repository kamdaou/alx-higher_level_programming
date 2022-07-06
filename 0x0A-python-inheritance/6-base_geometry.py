#!/usr/bin/python3
"""
6-base_geometry: contains Base Geometry class
"""


class BaseGeometry:
    """
    BaseGeometry class
    Methods:
        area: raises an Exception with the message area() is not implemented
    """
    def area(self):
        """
        raises an Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")
