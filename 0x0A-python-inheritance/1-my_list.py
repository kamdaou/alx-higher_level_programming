#!/usr/bin/python3
"""
1-my_list: contains MyList class
"""


class MyList(list):
    """
    It's a class that inherit from list.
    Attributes:
    Methods:
        print_sorted: prints a list in ascending way
    """
    def print_sorted(self):
        """
        Prints a list in ascending way
        :return: Nothing
        """
        sorted_list = sorted(self)
        print(sorted_list)
