#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = data
            self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node
    @next_node.setter
    def next_node(self, value):
        if value is not None or isinstance(value, Node) is True:
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList():
    def __init__(self):
        self.__head = None
    def __repr__(self):
        if head is None:
            print()
        else:
            node = self.__head
            while node is not None:
                print(node)
                node = node.next
