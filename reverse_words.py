"""
Write a reverseWords function that accepts a string a parameter,
and reverses each word in the string.
Every space should stay, so you cannot use words from Prelude.

Example:

reverse_words("This is an example!") # returns "sihT si na !elpmaxe"
"""


def reverse_words(s):
    return " ".join([word[::-1] for word in s.split(" ")])


from unittest import TestCase


class TestReverseWords(TestCase):
    def test_reverse_words(self):
        self.assertEquals(reverse_words('This is an example!'), 'sihT si na !elpmaxe')