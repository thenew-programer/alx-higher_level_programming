#!/usr/bin/python3
"""
This class will be the “base” of all other classes in this project.
The goal of it is to manage id attribute in all your future classes
and to avoid duplicating the same code (by extension, same bugs)
"""
import json
import csv
import turtle


class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
        
    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            if not list_objs:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dicts))


    @staticmethod
    def from_json_string(list_dictionaries):
        if not list_dictionaries or list_dictionaries is None:
            return []
        return json.loads(list_dictionaries)

    @classmethod
    def create(cls, **dictionary):
        if dictionary:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as f:
                list_dicts = Base.from_json_string(f.read())
                return [cls.create(**kwargs) for kwargs in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = str(cls.__name__) + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if not list_objs:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#000000")
        turt.pensize(3)
        turt.shape("turtle")
        turt.goto(-300, 200)

        turt.color("#ffffff")
        for rect in list_rectangles:
            pos = turt.pos()
            turt.showturtle()
            turt.up()
            turt.goto(rect.x + pos[0] + 10, rect.y - pos[1] - 10)
            turt.down()
            for i in range(2):
                turt.fd(rect.width)
                turt.lt(90)
                turt.fd(rect.height)
                turt.lt(90)
            turt.hideturtle()

        turt.color("#ffffff")
        for sq in list_squares:
            pos = turt.pos()
            turt.showturtle()
            turt.up()
            turt.goto(sq.x + pos[0] + 10, sq.y - pos[1] - 10)
            turt.down()
            for _ in range(2):
                turt.fd(sq.width)
                turt.lt(90)
                turt.fd(sq.height)
                turt.lt(90)
            turt.hideturtle()

        turtle.exitonclick()
