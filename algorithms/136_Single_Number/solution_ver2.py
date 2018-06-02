# https://leetcode.com/problems/single-number/description/

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        o(n) but need extra space for set(nums)
        """
        return sum(set(nums)) * 2 - sum(nums)