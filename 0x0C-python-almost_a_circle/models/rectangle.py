#!/usr/bin/python3
"""

"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.__width == 0 or self.__height == 0:
            print("")

        [print() for _ in range(self.y)]
        for _ in range(self.height):
            [print(" ", end="") for _ in range(self.x)]
            [print("#", end="") for _ in range(self.width)]
            print()

    def update(self, *args, **kwargs):
        """Update instance attributes of the class"""
        if args:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                return
        else:
            for key, value in kwargs.items():
                match key:
                    case "id":
                        self.id = value
                    case "width":
                        self.width = value
                    case "height":
                        self.width = value
                    case "x":
                        self.x = value
                    case "y":
                        self.y = value

    def to_dictionary(self):
        rec_info = {}
        rec_info.update({"id": self.id})
        rec_info.update({"width": self.width})
        rec_info.update({"height": self.height})
        rec_info.update({"x": self.x})
        rec_info.update({"y": self.y})
        return rec_info


    def __str__(self):
        """method called by print or str"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
