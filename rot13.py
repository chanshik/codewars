"""
ROT13 is a simple letter substitution cipher that
replaces a letter with the letter 13 letters after it in the alphabet.
ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13.
If there are numbers or special characters included in the string,
they should be returned as they are.
Only letters from the latin/english alphabet should be shifted,
like in the original Rot13 "implementation".

Please note that using "encode" in Python is considered cheating.
"""

import string
from codecs import encode as _dont_use_this_


def rot13(message):
    cipher_table = {}
    for ch in range(0, 26):
        cipher_table[chr(ch + ord('A'))] = chr(((ch + 13) % 26) + ord('A'))
        cipher_table[chr(ch + ord('a'))] = chr(((ch + 13) % 26) + ord('a'))

    return "".join([cipher_table[c] if c in cipher_table else c for c in message])


from unittest import TestCase


class TestRot13(TestCase):
    def test_rot13(self):
        self.assertEquals(rot13("test"), "grfg")
        self.assertEquals(rot13("Test"), "Grfg")
