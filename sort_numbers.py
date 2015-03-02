"""
Finish the solution so that it sorts the passed in array of numbers.
If the function passes in an empty array or null/nil value then it should return an empty array.

For example:

solution([1,2,3,10,5]) # should return [1,2,3,5,10]
solution(None) # should return []
"""

def solution(nums):
    if not nums:
        return []

    return sorted(nums)


from unittest import TestCase

class TestSortNumbers(TestCase):
    def test_sort_numbers(self):
        self.assertEquals(solution([1,2,3, 10,5]), [1,2,3, 5,10])
        self.assertEquals(solution([1,2,10,5]), [1,2,5,10])
        self.assertEquals(solution(None), [])