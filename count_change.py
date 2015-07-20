"""
Write a function that counts how many different ways you can make change for an amount of money,
given an array of coin denominations.

For example, there are 3 ways to give change for 4 if you have coins with denomination 1 and 2:

1+1+1+1, 1+1+2, 2+2.
The order of coins does not matter:

1+1+2 == 2+1+1
Also, assume that you have an infinite ammount of coins.

Your function should take an amount to change and an array of unique denominations for the coins:

  count_change(4, [1,2]) # => 3
  count_change(10, [5,2,3]) # => 4
  count_change(11, [5,7]) # => 0
"""

def solve(n, coins, k):
    """
    Solution for count_change

    :param n: money
    :param coins: List of coins.
    :param k: coins[k]
    :return: Count of combinations.
    """

    # print("n: %d, k: %d" % (n, k))
    if k < 0 or n < 0:
        return 0

    if n == 0:  # Change for 0 is only empty one.
        return 1

    # print("  n: %d, k: %d" % (n, k - 1))
    # print("  n: %d, k: %d" % (n - coins[k], k))

    # solve(n, coins, k - 1) -> Count of money without coins[k]
    # solve(n - coins[k], coins, k) -> Count of (money - coins[k]) with coins[k]
    count = solve(n, coins, k - 1) + solve(n - coins[k], coins, k)

    # print("Count: %d" % count)
    return count


def count_change(money, coins):
    return solve(money, coins, len(coins) - 1)

from unittest import TestCase


class TestCountChange(TestCase):
    def test_count_change(self):
        self.assertEquals(3, count_change(4, [1,2]))
        self.assertEquals(4, count_change(10, [5,2,3]))
        self.assertEquals(0, count_change(11, [5,7]))