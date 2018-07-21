#  https://leetcode.com/problems/rotate-array/description/

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        # actually this is o(n) space, and probably not good for interview
        """
        shift = k % len(nums)
        nums[:] = nums[-shift:] + nums[:-shift]
