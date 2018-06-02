# https://leetcode.com/problems/single-number/description/
from functools import reduce


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        o(n) but need extra space for set(nums)
        """
        return reduce(lambda x, y: x^y, nums)