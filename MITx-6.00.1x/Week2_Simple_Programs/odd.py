
"""
Exercise: odd

Write a Python function, odd, that takes in one number and returns True when 
the number is odd and False otherwise.

You should use the % (mod) operator, not if.

This function takes in one number and returns a boolean.
"""
def odd(num:int):
    """
    Odd function
    :param num: int
    :return: True if num is odd, False otherwise
    """
    return not(num%2==0)
