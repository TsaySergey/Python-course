# Enter you module contents here
'''
Module: triangle

This module provides functions for calculating properties of right-angled triangles.

Functions:
- area_of_right_triangle(a, b): Computes the area of a right-angled triangle given its two perpendicular sides.
- hypotenuse(a, b): Computes the length of the hypotenuse of a right-angled triangle given its two perpendicular sides.

Module attributes:
- __version__: 1.0
- __author__: Your Name
'''

import math

__version__ = "1.0"
__author__ = "Sergey Tsay"

def hypotenuse(a,b):
    """
    Calculate the area of a right-angled triangle.

    Args:
    a (float or int): Length of one perpendicular side.
    b (float or int): Length of the other perpendicular side.

    Returns:
    float: Area of the right-angled triangle.
    """
    c = math.sqrt(a**a + b**b)
    return c 

def area(a,b):
    """
    Calculate the length of the hypotenuse of a right-angled triangle.

    Args:
    a (float or int): Length of one perpendicular side.
    b (float or int): Length of the other perpendicular side.

    Returns:
    float: Length of the hypotenuse.
    """
    c = 0.5 * a * b
    return c