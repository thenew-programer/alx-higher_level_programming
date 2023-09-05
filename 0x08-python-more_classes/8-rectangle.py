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

    :method area: public methond -> int
    :method perimeter: public method -> int
    """
    number_of_instances = 0
    print_symbol = '#'

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
            Rectangle.number_of_instances += 1

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

    def area(self):
        """ public method that returns the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """ public method that returns the perimeter of the rectangle"""
        if 0 in (self.__width, self.__height):
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []
        for i in range(self.__height):
            for _ in range(self.__width):
                rectangle.append(str(self.print_symbol))
            if i != self.__height - 1:
                rectangle.append("\n")
        return "".join(rectangle)

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1
