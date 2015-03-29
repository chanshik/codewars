"""
Write a function that returns all of the sublists of a list or Array.

Your function should be pure; it cannot modify its input.

Example:

power([1,2,3])
# => [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

For more details regarding this, see the power set entry in wikipedia.
"""


def power(s):
    len_s = len(s)
    max_n = 2 ** len_s
    results = []

    for i in xrange(max_n):
        bin_table = bin(i)[2:].rjust(len_s, '0')

        sub_list = []
        for j in xrange(len_s):
            if bin_table[len_s - j - 1] == '1':
                sub_list.append(s[j])

        results.append(sub_list)

    return results

from unittest import TestCase


class TestPower(TestCase):
    def test_power(self):
        self.assertEqual([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]], power([1, 2, 3]))