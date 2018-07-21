#  https://leetcode.com/problems/rotate-array/description/

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        # o(1) space
        [1,2,3,4,5], k = 2
        1. reverse whole thing -> [5,4,3,2,1]
        2. reverse first k -> [4,5,3,2,1]
        3. reverse from k on -> [4,5,1,2,3]
        """

        def reverse_section(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)
        k = k % n
        # careful with the indices
        reverse_section(nums, 0, n - 1)
        reverse_section(nums, 0, k - 1)
        reverse_section(nums, k, n - 1)
