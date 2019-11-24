
"""
Exercise: power iter

Write an iterative function iterPower(base, exp) that calculates the exponential 
base^exp by simply using successive multiplication. For example, iterPower(base, exp) 
should compute base^exp by multiplying base times itself exp times. 
Write such a function below.

This function should take in two values - base can be a float or an integer; 
exp will be an integer ≥ 0. It should return one numerical value. 
Your code must be iterative - use of the ** operator is not allowed.
"""
def pow_i(base, exp):
    """
    :param base: int, float, base of computation
    :param exp: int, number which power
    :return: int, base^exp
    """
    res=1
    for i in range(exp):
        res = res*base
    return res
