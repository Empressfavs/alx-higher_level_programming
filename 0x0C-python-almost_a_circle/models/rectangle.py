#!/usr/bin/python3
"""
Defines Rectangle class inherited from base

classes:
    -   Rectangle: class that defines and creates rectangles
        * Base - superclass
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherites from Base class
    and performs its rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization function

        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
            x(int): space around the width
            y(int): space around the height
            id(int): id of the rectangle
                        increases when another rectangle is added
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #
        """
        if self.width == 0 or self.height == 0:
            print("")
        for i in range(self.y):
            print("")
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Update the class Rectangle by overriding the __str__ method
        """
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} \
- {self.width}/{self.height}")

    def to_dictionary(self):
        """
        returns the dictionary representation of a Rectangle
        """
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
