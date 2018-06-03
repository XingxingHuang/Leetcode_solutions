#  https://leetcode.com/problems/find-the-duplicate-number/solution/


class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        # time O(nlogn)  sort
        # space O(1) for i
        # but sort modifies nums
        """
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
