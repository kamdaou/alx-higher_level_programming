#!/usr/bin/python3
"""
    8-rectangle: class Rectangle from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Inherits BaseGeometry
    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
    Methods:
        __init__: initializes weight and height
        area: Calculate the area of the rectangle
    """

    def __init__(self, width, height):
        """
        instatiation with height and width
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        calculate area of the rectangle
        Return:
            an integer
        """
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
