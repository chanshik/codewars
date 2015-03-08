"""
Create a function add(n) which returns a function that always adds n to any number

addOne = add(1)
addOne(3) # 4

addThree = add(3)
addThree(3) # 6
"""

def add(n):
    return lambda x: x + n


from unittest import TestCase

class TestAdd(TestCase):
    def test_add(self):
        self.assertEqual(4, add(1)(3))
        self.assertEqual(6, add(3)(3))