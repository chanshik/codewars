"""
The prime factorization of a positive integer is a list of the integer's prime factors,
together with their multiplicities;
the process of determining these factors is called integer factorization.
The fundamental theorem of arithmetic says that
every positive integer has a single unique prime factorization.

The prime factorization of 24, for instance, is (2^3) * (3^1).

Without using the prime library, write a class called PrimeFactorizer
that takes in an integer greater than 1 and has a method called factor
which returns a hash where the keys are prime numbers
and the values are the multiplicities.

PrimeFactorizer(24).factor #should return { 2: 3, 3: 1 }
"""
from collections import defaultdict
from math import sqrt


class PrimeFactorizer(object):
    def __init__(self, n):
        self.factor = self.calc_factor(n)

    @staticmethod
    def is_prime(n):
        if n <= 1:
            return False

        max_n = int(sqrt(n) + 1)
        for i in xrange(2, max_n):
            if n % i == 0:
                return False

        return True

    @staticmethod
    def calc_factor(target):
        factors = defaultdict(int)
        n = target

        for i in xrange(2, n + 1):
            if not PrimeFactorizer.is_prime(i):
                continue

            while n % i == 0:
                n /= i
                factors[i] += 1

            if n <= 1:
                break

        return dict(factors)


from unittest import TestCase


class TestPrimeFactorizer(TestCase):
    def test_PrimeFactorizer(self):
        self.assertEquals(PrimeFactorizer(13).factor, {13: 1})
        self.assertEquals(PrimeFactorizer(24).factor, {2: 3, 3: 1})