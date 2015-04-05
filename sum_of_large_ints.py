"""
http://www.codewars.com/kata/sum-of-large-ints/train/python

Write this function

for i from 1 to n, do i % m and return the sum

f(n=10, m=5) // returns 20 (1+2+3+4+0 + 1+2+3+4+0)
"""


def f(n, m):
    group_count = n / m
    group_sum = m * (m - 1) / 2
    remain = n % m
    remain_sum = (1 + remain) * remain / 2

    return group_sum * group_count + remain_sum

from unittest import TestCase


class TestSumLargeInts(TestCase):
    def test_sum_of_large_ints(self):
        # self.assertEquals(f(10, 5), 20)
        # self.assertEquals(f(20, 20), 190)
        # self.assertEquals(f(15, 10), 60)
        # self.assertEquals(f(1000000, 2000000), 500000500000)
        # self.assertEquals(f(36221190, 16923028), 309306720117610)

        # self.assertEquals(f(515679, 13855585), 3705479524128)
        self.assertEquals(f(13855585, 515679), 3705479524128)