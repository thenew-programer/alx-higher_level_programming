#!/usr/bin/python3
"""
child class of BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    child class of BaseGeometry
    Args:
        width (int): The width of the new Rectangle.
        height (int): The height of the new Rectangle.
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
