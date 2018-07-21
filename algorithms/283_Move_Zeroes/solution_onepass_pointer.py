class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast , num in enumerate(nums):
            if num != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1