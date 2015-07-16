"""
Given an array of positive or negative integers

I= [i1,..,in]

you have to produce a sorted array P of the form

[ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

P will be sorted by increasing order of the prime numbers.
The final result has to be given as a string in Java or C# and as an array of arrays in other languages.

Example:

I = [12, 15]
result = [[2, 12], [3, 27], [5, 15]]
[2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

Note: It can happen that a sum is 0 if some numbers are negative!

Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in the result,
the sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result amongst others.
"""
from collections import defaultdict
from math import sqrt


def is_prime(n, cached_dict=None):
    if n <= 1:
        return False

    if cached_dict is not None and n in cached_dict:
        return cached_dict[n]

    max_n = int(sqrt(n) + 1)
    for i in xrange(2, max_n):
        if n % i == 0:
            if cached_dict is not None:
                cached_dict[n] = False

            return False

    if cached_dict is not None:
        cached_dict[n] = True

    return True


def calc_factor(target, cached_dict=None):
    factors = defaultdict(int)
    n = target

    for i in xrange(2, n + 1):
        if not is_prime(i, cached_dict):
            continue

        while n % i == 0:
            n /= i
            factors[i] += 1

        if n <= 1:
            break

    return dict(factors)


def sum_for_list(l):
    sum_by_factors = defaultdict(int)
    cached_dict = dict()

    for item in l:
        factors = calc_factor(abs(item), cached_dict)

        for k in sorted(factors.keys()):
            sum_by_factors[k] += item

    results = list()
    for factor in sorted(sum_by_factors.keys()):
        results.append([factor, sum_by_factors[factor]])

    return results

print(sum_for_list([12, 15]))
print(sum_for_list([15, 30, -45]))

# from unittest import TestCase
#
#
# class TestSumForList(TestCase):
#     def test_sum_for_list(self):
#         self.assertEquals(sum_for_list([12, 15]), [[2, 12], [3, 27], [5, 15]])
#         self.assertEquals(sum_for_list([15, 30, -45]), [[2, 30], [3, 0], [5, 0]])