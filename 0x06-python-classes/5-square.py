#!/usr/bin/python3
""" calsszs Define"""
class Square:
    """square class"""

    def __init__(self, size=0):
        """ienitialisation size
        Args: size - size sduare
        raises: TypeError or Valueerror
        """
        if size < 0:
            raise ValueError('size must be >= 0')
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        self.__size = size

    @property
    def size(self):
        """ienitialisation size
        Args: size - size sduare
        raises: TypeError or Valueerror"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """ienitialisation size
        Args: size - size sduare
        raises: TypeError or Valueerror"""
        if size < 0:
            raise ValueError('size must be >= 0')
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        self.__size = size

    def area(self):
        """area square"""

        return (self.__size ** 2)

    def my_print(self):
        """print the square #"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size))
