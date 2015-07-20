"""
Scientists working internationally use metric units almost exclusively.
Unless that is, they wish to crash multimillion dollars worth of equipment on Mars.

Your task is to write a simple function that takes a number of meters,
and outputs it using metric prefixes.

In practice, meters are only measured in "mm" (thousandths of a meter),
"cm" (hundredths of a meter), "m" (meters) and "km" (kilometers, or clicks for the US military).

For this exercise we just want units bigger than a meter,
from meters up to yottameters, excluding decameters and hectometers.

All values passed in will be positive integers. e.g.

meters(5);
// returns "5m"

meters(51500);
// returns "51.5km"

meters(5000000);
// returns "5Mm"
"""


def meters(x):
    from collections import OrderedDict

    factor_prefix_dict = OrderedDict([
        (1000000000000000000000000L, "Ym"),
        (1000000000000000000000L, "Zm"),
        (1000000000000000000L, "Em"),
        (1000000000000000L, "Pm"),
        (1000000000000, "Tm"),
        (1000000000, "Gm"),
        (1000000, "Mm"),
        (1000, "km"),
        (1, "m")
    ])

    for factor in factor_prefix_dict.keys():
        print("x: %d, factor: %f" % (x, factor))
        if x >= factor:
            result = str(float(x / float(factor))) + factor_prefix_dict[factor]

            return result.replace(".0", "")

from unittest import TestCase


class TestMeters(TestCase):
    def test_meters(self):
        self.assertEquals("1m", meters(1))
        self.assertEquals("1km", meters(1000))
        self.assertEquals("12.3Mm", meters(12300000))
        self.assertEquals("10Ym", meters(10000000000000000000000000))