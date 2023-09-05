#!/usr/bin/python3
"""defines a function called say_my_name"""


def say_my_name(first_name, last_name=""):
   """prints 'My name is <first_name> <last_name>'
   :param first_name: (str)
   :param last_name: (str)
   """ 
   if type(first_name) != str:
       raise TypeError("first_name must be a string")
   if type(last_name) != str:
       raise TypeError("last_name must be a string")

   print(f"My name is {first_name} {last_name}")


if __name__ == "__main__":
    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")
    try:
        say_my_name(12, "White")
    except Exception as e:
        print(e)
