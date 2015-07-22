"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
"""
import re


def solution(text, markers):
    if len(markers) == 0:
        return text

    escaped_markers = ['\\' + marker for marker in markers]
    searcher = re.compile(r"[%s]" % "".join(escaped_markers))

    results = []
    for line in text.split('\n'):
        res = searcher.search(line)
        if res is None:
            results.append(line)
            continue

        results.append(line[:res.span()[0]].rstrip())

    return "\n".join(results)

from unittest import TestCase


class TestStripComment(TestCase):
    def test_solution(self):
        self.assertEqual(
            solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]),
            "apples, pears\ngrapes\nbananas")
        self.assertEqual(
            solution("a #b\nc\nd $e f g", ["#", "$"]),
            "a\nc\nd")