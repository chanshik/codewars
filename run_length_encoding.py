# coding=utf-8
"""
Task

Your task is to write such a run-length encoding.
For a given string, return a list (or array) of pairs (or arrays) [ (i1, s1), (i2, s2), …, (in, sn) ],
such that one can reconstruct the original string by replicating the character sx ix times
and concatening all those strings.
Your run-length encoding should be minimal,
ie. for all i the values si and si+1 should differ.

Examples

As the article states, RLE is a very simple form of data compression.
It's only suitable for runs of data, as one can see in the following example:

run_length_encoding("hello world!")
 //=>      [[1,'h'],[1,'e'],[2,'l'],[1,'o'],[1,' '],[1,'w'],[1,'o'],[1,'r'],[1,'l'],[1,'d'],[1,'!']]

It's very effective if the same data value occurs in many consecutive data elements:

run_length_encoding("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb")
# => [[34,'a'], [3,'b']]
"""


def run_length_encoding(s):
    if len(s) == 0:
        return []

    last_idx = len(s) - 1
    cur_ch = s[0]
    cur_len = 1
    rle = []

    for idx in range(1, len(s)):
        if s[idx] != cur_ch:
            rle.append([cur_len, cur_ch])
            cur_ch = s[idx]
            cur_len = 1
        else:
            cur_len += 1

        if idx == last_idx:
            rle.append([cur_len, cur_ch])

    return rle


from unittest import TestCase


class TestRLE(TestCase):
    def test_run_length_encoding(self):
        self.assertEquals(run_length_encoding(''), [])
        self.assertEquals(run_length_encoding("abc"), [[1, 'a'], [1, 'b'], [1, 'c']])
        self.assertEquals(run_length_encoding("aab"), [[2, 'a'], [1, 'b']])
        self.assertEquals(
            run_length_encoding("hello world!"),
            [[1, 'h'], [1, 'e'], [2, 'l'], [1, 'o'], [1, ' '], [1, 'w'], [1, 'o'], [1, 'r'], [1, 'l'],
             [1, 'd'], [1, '!']])
        self.assertEquals(
            run_length_encoding("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb"),
            [[34, 'a'], [3, 'b']])