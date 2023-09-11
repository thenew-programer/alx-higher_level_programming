#!/usr/bin/python3
"""class MyList that inherites from list class"""


class MyList(list):
    def __init__(self, arr=[]):
        super().__init__(arr)

    def print_sorted(self):
        print(sorted(self))
