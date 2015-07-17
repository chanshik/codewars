"""
Write a module Converter that can take ASCII text and convert it to hexadecimal.
The class should also be able to take hexadecimal and convert it to ASCII text.

Example

Converter.to_hex("Look mom, no hands")
=> "4c6f6f6b206d6f6d2c206e6f2068616e6473"

Converter.to_ascii("4c6f6f6b206d6f6d2c206e6f2068616e6473")
=> "Look mom, no hands"
"""


class Converter():
    @staticmethod
    def to_ascii(h):
        return "".join([chr(int("".join(item), 16)) for item in zip(h[::2], h[1::2])])

    @staticmethod
    def to_hex(s):
        return "".join([hex(ord(item))[2:] for item in s])

from unittest import TestCase


class TestConverter(TestCase):
    def test_to_hex(self):
        s = "Look mom, no hands"
        h = "4c6f6f6b206d6f6d2c206e6f2068616e6473"
        self.assertEquals(Converter.to_hex(s), h)

    def test_converter(self):
        s = "Look mom, no hands"
        h = "4c6f6f6b206d6f6d2c206e6f2068616e6473"

        self.assertEquals(Converter.to_hex(s), h)
        self.assertEquals(Converter.to_ascii(h), s)
        self.assertEquals(Converter.to_hex(Converter.to_ascii(h)), h)
        self.assertEquals(Converter.to_ascii(Converter.to_hex(s)), s)