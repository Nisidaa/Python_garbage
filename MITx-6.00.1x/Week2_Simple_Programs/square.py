"""
Exercise: square

Write a Python function, square, that takes in one number and returns the square 
of that number.

This function takes in one number and returns one number.
"""


def square(x):
    """
    :param x: int, float of even str
    :return: square of input
    """
    if type(x) == int or type(x) == float:
        return x * x
    elif str.isdigit(x):
        return float(x) * float(x)
    else:
        raise TypeError

