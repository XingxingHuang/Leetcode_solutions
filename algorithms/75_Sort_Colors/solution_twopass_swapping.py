class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 1
        n = len(nums)
        while slow < n - 1:
            while fast <= n - 1:
                if nums[slow] > nums[fast]:
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                fast += 1
            slow += 1
            fast = slow + 1
