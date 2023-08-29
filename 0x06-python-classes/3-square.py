#!/usr/bin/python3
""" Defines a class named Square that sets an instance attribute
    to the value provided by the user based on some asumptions """


class Square:
    """ constructor - initialize a private instance attribute
        args:
            size (int): the private instance attribute
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """
    area - returns the area of the square
    """

    def area(self):
        return self.__size ** 2
