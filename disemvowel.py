"""
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels
from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
"""
def disemvowel(string):
    import re

    rx = re.compile('([aeouiAEOUI])')

    return rx.sub('', string)


from unittest import TestCase

class TestDisemVowel(TestCase):
    def test_disemvowel(self):
        self.assertEquals(
            disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")
        self.assertEqual(
            disemvowel("N ffns bt,\nYr wrtng s mng th wrst 'v vr rd"), "N ffns bt,\nr wrtng s mng th wrst 'v vr rd")