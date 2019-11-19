"""
Exercise: eval quadratic

Write a Python function, evalQuadratic(a, b, c, x), that returns the value of 
the quadratic a*(x*x) + b*x + c

This function takes in four numbers and returns a single number.
"""


def evalQuadratic(a, b, c, x):
    return a * (x * x) + b * x + c


print(evalQuadratic(1, 1, 2, 1))
