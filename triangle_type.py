# coding=utf-8
"""
In this kata, you should calculate type of triangle with three given sides a, b and c.

If all angles are less than 90°, this triangle is acute and function should return 1.

If one angle is strictly 90°, this triangle is right and function should return 2.

If one angle more than 90°, this triangle is obtuse and function should return 3.

If three sides cannot form triangle, or one angle is 180° (which turns triangle into segment)
 - function should return 0.

Input parameters are sides of given triangle.
All input values are non-negative floating point or integer numbers (or both).
"""

# Should return triangle type:
#  0 : if triangle cannot be made with given sides
#  1 : acute triangle
#  2 : right triangle
#  3 : obtuse triangle


def triangle_type(a, b, c):
    lengths = sorted([a, b, c])
    squares = map(lambda x: x * x, lengths)

    if lengths[0] + lengths[1] <= lengths[2]:
        return 0

    if squares[0] + squares[1] > squares[2]:
        return 1

    if squares[0] + squares[1] == squares[2]:
        return 2

    return 3


from unittest import TestCase


class TestTriangleType(TestCase):
    def test_triangle_type(self):
        self.assertEquals(triangle_type(7, 3, 2), 0)  # Not triangle
        self.assertEquals(triangle_type(2, 4, 6), 0)  # Not triangle
        self.assertEquals(triangle_type(8, 5, 7), 1)  # Acute
        self.assertEquals(triangle_type(3, 4, 5), 2)  # Right
        self.assertEquals(triangle_type(7, 12, 8), 3)  # Obtuse
