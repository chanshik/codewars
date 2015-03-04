"""
Welcome. In this kata you are required to, given a string,
replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
a being 1, b being 2, etc. As an example:

alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (As a string.)
"""


def alphabet_position(text):
    return " ".join([str(ord(c) - ord('A') + 1) for c in text.upper() if str.isalpha(c)])


from unittest import TestCase


class TestAlphabet(TestCase):
    def test_alphabet_position(self):
        from random import randint
        self.assertEquals(
            "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11",
            alphabet_position("The sunset sets at twelve o' clock."))
        self.assertEquals(
            "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20",
            alphabet_position("The narwhal bacons at midnight."))

        number_test = ""
        for item in range(10):
            number_test += str(randint(1, 9))
        self.assertEquals(alphabet_position(number_test), "")