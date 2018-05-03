# https://leetcode.com/problems/find-pivot-index/description/


class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftsum = 0
        rightsum = sum(nums)
        for idx, num in enumerate(nums):
            rightsum -= num
            if leftsum == rightsum:
                return idx
            leftsum += num
        return -1