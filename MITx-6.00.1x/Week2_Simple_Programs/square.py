"""
Exercise: square

Write a Python function, square, that takes in one number and returns the square 
of that number.

This function takes in one number and returns one number.
"""


def square(x):
    if type(x) == int or type(x) == float:
        return x * x
    elif str.isdigit(x):
        return float(x) * float(x)
    else:
        raise TypeError

