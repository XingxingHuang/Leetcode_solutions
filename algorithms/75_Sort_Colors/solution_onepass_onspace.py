class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums_copy = nums.copy()  # note python 2 list don't have copy
        n = len(nums)
        start = 0
        end = n - 1
        for idx, num in enumerate(nums_copy):
            if num == 0:
                nums[start] = 0
                start += 1
            if num == 2:
                nums[end] = 2
                end -= 1

        while start <= end:
            nums[start] = 1
            start += 1

