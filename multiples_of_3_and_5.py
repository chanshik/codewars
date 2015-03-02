"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all
the multiples of 3 or 5 below the number passed in.
"""
def solution(number):
    sum_of_3 = sum(range(3, number, 3))
    sum_of_5 = sum(range(5, number, 5))
    sum_of_intersect = sum(range(15, number, 15))

    return sum_of_3 + sum_of_5 - sum_of_intersect


from unittest import TestCase

class TestMultiples(TestCase):
    def test_multiples(self):
        self.assertEquals(solution(10), 23)