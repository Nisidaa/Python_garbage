"""
Exercise: fourth power

Write a Python function, fourthPower, that takes in one number and returns that 
value raised to the fourth power.

You should use the square procedure that you defined in an earlier exercise 
(you don't need to redefine square in this box; when you call square, the grader 
 will use our definition).

This function takes in one number and returns one number.
"""
from Week2_Simple_Programs.square import square
def fourthPower(x):
        return square(x) * square(x)
