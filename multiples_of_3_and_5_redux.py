# coding=utf-8
"""
The galactic games have begun!

It's the galactic games! Beings of all worlds come together
to compete in several interesting sports, like nroogring,
fredling and buzzing (the beefolks love the last one).
However, there's also the traditional marathon run.

Unfortunately, there have been cheaters in the last years,
and the committee decided to place sensors on the track.
Committees being committees, they've come up with the following rule:

    A sensor should be placed every 3 and 5 meters from the start, e.g. at 3m, 5m, 6m, 9m, 10m, 12m, 15m, 18m….

Since you're responsible for the track, you need to buy those sensors.
Even worse, you don't know how long the track will be!
And since there might be more than a single track,
and you can't be bothered to do all of this by hand,
you decide to write a program instead.

Task

Return the sum of the multiples of 3 and 5 below a number.
Being the galactic games, the tracks can get rather large,
so your solution should work for really large numbers (greater than 1,000,000).
Examples

solution (10) # => 23 = 3 + 5 + 6 + 9
solution (20) # => 78 = 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18
"""


def solution(number):
    def sum_of_sequence(start, diff, end):
        """
        Calculate sum of arithmetic sequence is
          Sn = n{2a + (n - 1)d} / 2

          a: start
          d: common difference
          n: nth term of the sequence
        """
        n = end / diff
        n = n - 1 if end % diff == 0 else n  # Upper bound

        return n * (2 * start + (n - 1) * diff) / 2

    sum_of_3 = sum_of_sequence(3, 3, number)
    sum_of_5 = sum_of_sequence(5, 5, number)
    sum_of_intersect = sum_of_sequence(15, 15, number)

    return sum_of_3 + sum_of_5 - sum_of_intersect


from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEquals(solution(10), 23)
        self.assertEquals(solution(20), 78)
        self.assertEquals(solution(100), 2318)
        self.assertEquals(solution(200), 9168)
        self.assertEquals(solution(1000), 233168)
        self.assertEquals(solution(10000), 23331668)
        self.assertEquals(
            solution(50000000000000000000000000000000000000000),
            583333333333333333333333333333333333333291666666666666666666666666666666666666668L)