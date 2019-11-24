
"""
Exercise: power recur

Write a function recurPower(base, exp) which computes base^exp by recursively 
calling itself to solve a smaller version of the same problem, and then 
multiplying the result by base to solve the initial problem.

This function should take in two values - base can be a float or an integer; 
exp will be an integer ≥0. It should return one numerical value. Your code 
must be recursive - use of the ** operator or looping constructs is not allowed.
"""
def pow_r(base, exp):
    """
      :param base: int, float base of computation
      :param exp: int, number which power
      :return: int, base^exp
      """
    if exp==1:
        return base
    else: return base * pow_r(base, exp-1)