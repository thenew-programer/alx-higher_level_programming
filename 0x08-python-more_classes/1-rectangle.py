#!/usr/bin/python3
"""define a class representing a rectangle"""


class Rectangle:
    """ class that hold the width and height of a rectangle
    :attribute width: (int)
    :attribute height: (int)

    :method width: getter -> int
    :method width: setter -> void

    :method height: getter -> int
    :method height: setter -> void
    """
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = width
            self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
