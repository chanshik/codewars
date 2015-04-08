"""
Two Joggers
Description

Bob and Charles are meeting for their weekly jogging tour.
They both start at the same spot called "Start" and
they each run a different lap, which may (or may not) vary in length.
Since they know each other for a long time already,
they both run at the exact same speed.

Illustration

Example where Charles (dashed line) runs a shorter lap than Bob:

Example laps
Task

Your job is to complete the function nbrOfLaps(x, y) that,
given the length of the laps for Bob and Charles,
finds the number of laps that each jogger has to complete
before they meet each other again, at the same time, at the start.

The function takes two arguments:

    The length of Bob's lap (larger than 0)
    The length of Charles' lap (larger than 0)

The function should return an array containing exactly two numbers:

    The first number is the number of laps that Bob has to run
    The second number is the number of laps that Charles has to run

Examples

nbr_of_laps(5, 3) # returns [3,5]
nbr_of_laps(4, 6); # returns [3, 2]
"""


def nbr_of_laps(x, y):
    a, b = x, y
    remain = a % b
    while remain > 0:
        a, b = b, remain
        remain = a % b

    gcd = b
    lcm = x * y / gcd

    return lcm / x, lcm / y

from unittest import TestCase


class TestNumberOfLaps(TestCase):
    def test_nbr_of_laps(self):
        self.assertTrue(nbr_of_laps(5, 3)[0] == 3,
                        'x = 5, y = 3 The number of laps for Bob is wrong. Expected 3, got {}'.format(
                            nbr_of_laps(5, 3)[0]))
        self.assertTrue(nbr_of_laps(5, 3)[1] == 5,
                        'x = 5, y = 3 The number of laps for Charles is wrong. Expected 5, got {}'.format(
                            nbr_of_laps(5, 3)[1]))
        self.assertTrue(nbr_of_laps(4, 6)[0] == 3,
                        'x = 4, y = 6 The number of laps for Charles is wrong. Expected 3, got {}'.format(
                            nbr_of_laps(4, 6)[0]))
        self.assertTrue(nbr_of_laps(4, 6)[1] == 2,
                        'x = 4, y = 6 The number of laps for Charles is wrong. Expected 2, got {}'.format(
                            nbr_of_laps(4, 6)[1]))
        self.assertTrue(nbr_of_laps(5, 5)[0] == 1,
                        'x = 5, y = 5 The number of laps for Bob is wrong. Expected 1, got {}'.format(
                            nbr_of_laps(5, 5)[0]))
        self.assertTrue(nbr_of_laps(5, 5)[1] == 1,
                        'x = 5, y = 5 The number of laps for Charles is wrong. Expected 1, got {}'.format(
                            nbr_of_laps(5, 5)[1]))