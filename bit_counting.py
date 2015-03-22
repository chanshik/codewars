"""
Write a function that takes an (unsigned) integer as input,
and returns the number of bits that are equal to one in the binary
representation of that number.

Example: The binary representation of 1234 is 10011010010,
so the function should return 5 in this case

"""


def countBits(n):
    bits = 0

    while n > 0:
        if n & 1:
            bits += 1

        n /= 2

    return bits

from unittest import TestCase


class TestCountBits(TestCase):
    def test_count_bits(self):
        self.assertEquals(countBits(0), 0)
        self.assertEquals(countBits(4), 1)
        self.assertEquals(countBits(7), 3)
        self.assertEquals(countBits(9), 2)
        self.assertEquals(countBits(10), 2)