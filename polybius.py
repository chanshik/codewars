"""
Implement the Polybius square cipher.

Replace every letter with a two digit number.
The first digit is the row number,
and the second digit is the column number of following square.
Letters 'I' and 'J' are both 24 in this cipher:

    1	2	3	4	5
1	A	B	C	D	E
2	F	G	H	I/J	K
3	L	M	N	O	P
4	Q	R	S	T	U
5	V	W	X	Y	Z

Input will be valid (only spaces and uppercase letters from A to Z),
so no need to validate them.

Examples:

polybius('A') # "11"
polybius('POLYBIUS SQUARE CIPHER') # "3534315412244543 434145114215 132435231542"
polybius('IJ') # "2424"
polybius('CODEWARS') # "1334141552114243"

"""


def polybius(text):
    def cipher(letter):
        if letter == ' ':
            return ' '

        pos = ord(letter) - 65
        pos = pos - 1 if pos > 8 else pos

        return '%d%d' % (pos / 5 + 1, pos % 5 + 1)

    return "".join([cipher(ch) for ch in text])

from unittest import TestCase


class TestPolybius(TestCase):
    def test_polybius(self):
        self.assertEquals(polybius('CODEWARS'), '1334141552114243')
        self.assertEquals(
            polybius('POLYBIUS SQUARE CIPHER'), '3534315412244543 434145114215 132435231542')