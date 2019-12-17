"""
Grader

A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is: (0.25∗n∗s^2)/tan(π/n)

The perimeter of a polygon is: length of the boundary of the polygon

Write a function called polysum that takes 2 arguments, n and s. This function 
should sum the area and square of the perimeter of the regular polygon. The 
function returns the sum, rounded to 4 decimal places.
"""
import math


def polysum(n, s):
    """
    :return: sum the area and square of the perimeter of the regular polygon
    :param n: number of sides
    :param s: length of side
    """
    area = (0.25 * n * pow(s, 2)) / math.tan(math.pi / n)
    perimeter = n * s
    return float("{0:.4f}".format(area + pow(perimeter, 2)))

#test
# n = 5, s = 2, ans = 106.2219
print(polysum(5, 2))