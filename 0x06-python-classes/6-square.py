#!/usr/bin/python3
""" Defines a class named Square that sets an instance attribute
    to the value provided by the user based on some asumptions """


class Square:
    """ constructor - initialize a private instance attribute
        args:
            size (int): the private instance attribute
    """
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if type(position) is not tuple or
        type(position[0]) is not int or
        type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position
    """
    area - returns the area of the square
    """

    def area(self):
        return self.__size ** 2
    """
    size - getter : gets the __size attribute
    """
    @property
    def size(self):
        return self.__size
    """
    size - setter : change the  __size attribute
    args:
        value (int): the value we want to set to our var
    """
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
