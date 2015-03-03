"""
Santa puts all the presents into the huge sack.
In order to let his reindeers rest a bit,
he only takes as many reindeers with him as he is required to do.
The others may take a nap.

Two reindeers are always required for the sleigh and Santa himself.
Additionally he needs 1 reindeer per 30 presents. As you know,
Santa has 8 reindeers in total, so he can deliver up to 180 presents at once
(2 reindeers for Santa and the sleigh + 6 reindeers with 30 presents each).

Complete the function reindeers(), which takes a number of presents and
returns the minimum numbers of required reindeers.
If the number of presents is too high, throw an error.

Examles:

reindeer(0) # must return 2
reindeer(1) # must return 3
reindeer(30) # must return 3
reindeer(200) # must throw an error

"""


def reindeer(presents):
    from math import ceil

    # Each reindeer can carry 30 presents.
    reindeers = ceil(presents / 30.0) + 2

    if reindeers > 8:
        raise Exception

    return reindeers


from unittest import TestCase


class TestReindeer(TestCase):
    def test_reindeer(self):
        self.assertEquals(reindeer(0), 2, '0 present')
        self.assertEquals(reindeer(1), 3, '1 present')
        self.assertEquals(reindeer(30), 3, '30 presents')
        self.assertEquals(reindeer(180), 8, '180 presents')
        self.assertEquals(reindeer(179), 8, '179 presents')

        self.assertRaises(Exception, reindeer, 181)
        self.assertRaises(Exception, reindeer, 200)
