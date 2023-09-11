#!/usr/bin/python3
"""
class BaseGeometry
"""


class BaseGeometry:
    """
    Represent base geometry

    method:
        area(void) -> nothing: raise an Exeption

        integer_validator(name: str, value: any) -> nothing: raise TypeError and ValueError
        based on the type of value
    """
    def area(self):
        """
        unimplemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
         validates value

         Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

