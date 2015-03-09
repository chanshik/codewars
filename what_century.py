"""
Return the inputted numerical year in century format. For example 2014, would return 21st.

The input will always be a 4 digit string. So there is no need for year string validation

Examples:
Input: 1999 Output: 20th
Input: 2011 Output: 21st
Input: 2154 Output: 22nd
Input: 2259 Output: 23rd
Input: 1124 Output: 12th
Input: 2000 Output: 20th
"""

def whatCentury(year):
    ordinal = ['th', 'st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th',
               'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th']
    year = int(year)
    century = ((year - 1) / 100) + 1

    if century < 20:
        return "%d%s" % (century, ordinal[century % 20])
    else:
        return "%d%s" % (century, ordinal[century % 10])

from unittest import TestCase


class TestWhatCentury(TestCase):
    def test_what_century(self):
        self.assertEqual("20th", whatCentury("1999"))
        self.assertEqual("21st", whatCentury("2011"))
        self.assertEqual("22nd", whatCentury("2154"))
        self.assertEqual("23rd", whatCentury("2259"))
        self.assertEqual("12th", whatCentury("1124"))
        self.assertEqual("20th", whatCentury("2000"))
