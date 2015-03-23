"""
The rgb() method is incomplete.
Complete the method so that passing in RGB decimal values will result in a hexadecimal
representation being returned.
The valid decimal values for RGB are 0 - 255.
Any (r,g,b) argument values that fall out of that range should be rounded to the closest valid value.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
"""


def rgb(r, g, b):
    r, g, b = map(lambda x: 0 if x < 0 else 255 if x > 255 else x, [r, g, b])

    return "%s%s%s" % (format(r, "02X"), format(g, "02X"), format(b, "02X"))

from unittest import TestCase


class TestRGBtoHex(TestCase):
    def test_rgb_to_hex(self):
        self.assertEquals(rgb(0, 0, 0), "000000", "testing zero values")
        self.assertEquals(rgb(1, 2, 3), "010203", "testing near zero values")
        self.assertEquals(rgb(255, 255, 255), "FFFFFF", "testing max values")
        self.assertEquals(rgb(254, 253, 252), "FEFDFC", "testing near max values")
        self.assertEquals(rgb(-20, 275, 125), "00FF7D", "testing out of range values")