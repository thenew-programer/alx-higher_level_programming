#!/usr/bin/python3
"""square class inherits from rectangle"""
Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle):
    """Square class represent squares"""
    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
