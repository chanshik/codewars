"""
The dragon's curve is a self-similar fractal which can be obtained by a recursive method.

Starting with the string D0 = 'Fa', at each step simultaneously perform the following operations:

replace 'a' with: 'aRbFR'
replace 'b' with: 'LFaLb'

For example (spaces added for more visibility) :

1st iteration: Fa -> F aRbF R
2nd iteration: FaRbFR -> F aRbFR R LFaLb FR

After n iteration, remove 'a' and 'b'.
You will have a string with 'R','L', and 'F'. This is a set of instruction.
Starting at the origin of a grid looking in the (0,1) direction,
'F' means a step forward, 'L' and 'R' mean respectively turn left and right.
After executing all instructions,
the trajectory will give a beautiful self-replicating pattern called 'Dragon Curve'

The goal of this kata is to code a function which takes one parameter n,
the number of iterations needed and return the string of instruction as defined above. For example:

n=0, should return: 'F'
n=1, should return: 'FRFR'
n=2, should return: 'FRFRRLFLFR'

n should be a number and non-negative integer. All other case should return the empty string: ''.

"""


def Dragon(n):
    if not isinstance(n, int):
        return ''
    if n < 0:
        return ''

    s = 'Fa'

    for i in range(n):
        changed = list()

        for ch in s:
            if ch == 'a':
                changed.append('aRbFR')
            elif ch == 'b':
                changed.append('LFaLb')
            else:
                changed.append(ch)

        s = "".join(changed)

    return s.replace('a', '').replace('b', '')

from unittest import TestCase


class TestDragon(TestCase):
    def test_dragon(self):
        self.assertEquals('F', Dragon(0))
        self.assertEquals('FRFR', Dragon(1))
        self.assertEquals('FRFRRLFLFR', Dragon(2))