#!/usr/bin/python3
"""define classes for a singly_linked list"""

class Node:
    """represent a node in linked list"""

    def __init__(self, data, next_node=None):
        """Initialisation a new node
        args:
        data: the data of a new node
        next_node: the next node """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """set data"""
        return self.__data

    @data.setter
    def data(self, value):
        """sat data value"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """set node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not instance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """represent SinglyLinkedList"""


    def __init__(self):
        """initialize SinglyLinkedList"""

        self.__head = None

    def sorted_insert(self, value):
        """insert a new node
        args: value - the new node"""

        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            t = self.__head
            while (t.next_node is not None and t.next_node.data < value):
                t = t.next_node
            new.next_node = t.next_node
            t.next_node = new

    def __str__(self):
        """Define the print presentation"""
        list_1 = []
        t = self.__head
        while t is not None:
            list_1.apppend(str(t.data))
            t = t.next_node
            return ('\n'.join(list_1))
