"""
Description:

An anagram is the result of rearranging the letters of a word to produce a new word. (Ref wikipedia).

Note: anagrams are case insensitive

Examples

foefet is an anagram of toffee
Buckethead is an anagram of DeathCubeK

The challenge is to write the function isAnagram (or is_anagram in Python)
to return true if the word test is an anagram of the word original and false otherwise.
The function prototype is as given below:

def is_anagram(test, original):
  pass
"""


def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())


from unittest import TestCase


class TestAnagramDetection(TestCase):
    def test_is_anagram(self):
        self.assertTrue(is_anagram('Creative', 'Reactive'))
        self.assertTrue(is_anagram('toffee', 'foefet'))
        self.assertTrue(is_anagram('Buckethead', 'DeathCubeK'))