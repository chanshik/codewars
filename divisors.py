"""
Create a function named divisors that takes an integer and
returns an array with all of the integer's divisors
(except for 1 and the number itself).

If the number is prime return the string '(integer) is prime'
(use Either String a in Haskell).

Example:

divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
"""


def is_prime(n):
    from math import sqrt
    if n <= 1:
        return False

    max_n = int(sqrt(n) + 1)
    for i in range(2, max_n):
        if n % i == 0:
            return False

    return True


def divisors(n):
    from math import sqrt
    max_n = int(sqrt(n) + 1)

    divs = [(i, n / i) for i in xrange(2, max_n) if n % i == 0]

    if len(divs) == 0:
        return "%d is prime" % n
    else:
        return sorted(set([div for div_pair in divs for div in div_pair]))


from unittest import TestCase


class TestDivisors(TestCase):
    def test_divisors(self):
        self.assertEquals([3, 5], divisors(15))
        self.assertEquals([2, 3, 4, 6], divisors(12))
        self.assertEquals("13 is prime", divisors(13))