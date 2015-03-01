"""
In this kata you will create a function to check a non-negative input
to see if it is a prime number.

The function will take in a number and will return True
if it is a prime number and False if it is not.

A prime number is a natural number greater than 1
that has no positive divisors other than 1 and itself.

Examples

isPrime(0) is false
isPrime(1) is false
isPrime(2) is true
isPrime(11) is true
isPrime(12) is false
"""
from math import sqrt

def is_prime(n):
    from math import sqrt
    if n == 0 or n == 1:
        return False

    max_n = int(sqrt(n) + 1)
    for i in range(2, max_n):
        if n % i == 0:
            return False

    return True

from unittest import TestCase

class TestPrime(TestCase):
    def test_is_prime(self):
        self.assertEquals(is_prime(0),False)
        self.assertEquals(is_prime(1),False)
        self.assertEquals(is_prime(2),True)
        self.assertEquals(is_prime(11),True)
        self.assertEquals(is_prime(12),False)
        self.assertEquals(is_prime(571),True)
        self.assertEquals(is_prime(25),False)