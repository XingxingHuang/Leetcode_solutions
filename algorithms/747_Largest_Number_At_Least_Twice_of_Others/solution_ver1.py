# https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/


class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # solution using sort
        if len(nums) <= 1:
            return 0
        sorted_nums = sorted(nums.copy())
        return nums.index(sorted_nums[-1]) if sorted_nums[-1] >= 2 * sorted_nums[-2] else -1