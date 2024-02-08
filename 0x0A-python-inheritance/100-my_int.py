#!/usr/bin/python3
class MyInt(int):
    """
    A class representing an integer with inverted equality operators.
    """


    def __eq__(self, other):
        """
        Override the == operator.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the != operator
        """
        return super().__eq__(other)

