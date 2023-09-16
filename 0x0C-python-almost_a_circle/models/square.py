#!/usr/bin/python3
"""

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """

    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update instance attributes of the class"""
        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                return
        else:
            for key, value in kwargs.items():
                match key:
                    case "id":
                        self.id = value
                    case "size":
                        self.size = value
                    case "x":
                        self.x = value
                    case "y":
                        self.y = value


    def to_dictionary(self):
        sqr_info = {}
        sqr_info.update({"id": self.id})
        sqr_info.update({"size": self.height})
        sqr_info.update({"x": self.x})
        sqr_info.update({"y": self.y})
        return sqr_info

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
