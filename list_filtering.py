"""
In this kata you will create a function that
takes a list of non-negative integers and strings
and returns a new list with the strings filtered out.
"""

def filter_list(l):
    def is_positive(n):
        if not isinstance(n, int):
            return False

        if n < 0:
            return False

        return True

    return filter(is_positive, l)


from unittest import TestCase

class TestListFiltering(TestCase):
    def test_list_filtering(self):
        self.assertEquals(filter_list([1,2,'a','b']),[1,2])
        self.assertEquals(filter_list([1,'a','b',0,15]),[1,0,15])
        self.assertEquals(filter_list([1,2,'aasf','1','123',123]),[1,2,123])