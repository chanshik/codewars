"""
The Hamming Distance is a measure of similarity between two strings of equal length.
Complete the function so that it returns the number of positions where the input strings do not match.

Examples (in JavaScript):

hamming("I like turtles","I like turkeys")  //returns 3
hamming("Hello World","Hello World")  //returns 0
You can assume that the two input strings are of equal length.
"""


def hamming(lhs, rhs):
    return sum([1 for l, r in zip(lhs, rhs) if l != r])


from unittest import TestCase


class TestHamming(TestCase):
    def test_hamming(self):
        self.assertEqual(hamming("I like turtles","I like turkeys"), 3)
        self.assertEqual(hamming("Hello World","Hello World"), 0)