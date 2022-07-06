#!/usr/bin/python3

"""
10-square implements Square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defines a square
    Attributes:
        size (int): size of the square
    Methods:
        __init__: instation with size
    """

    def __init__(self, size):
        """
        Initializes the square after validation of size
        """
        self.integer_validator("size", size)

        super(Square, self).__init__(size, size)
        self.__size = size

    def area(self):
        """
        calculate the size of the square
        Return: an integer
        """
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
