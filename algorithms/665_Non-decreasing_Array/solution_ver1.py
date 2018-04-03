#  https://leetcode.com/problems/non-decreasing-array/description/


class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        one line, linear time solution
        """
        return sum(map(lambda t: t[0] - t[1] < 0, zip(nums[1:], nums[:-1]))) <= 1 and sum(map(lambda t: t[0] - t[1] < 0, zip(nums[2:], nums[:-2]))) <= 1