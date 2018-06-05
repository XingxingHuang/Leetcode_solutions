# https://leetcode.com/problems/sliding-window-maximum/description/

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        loop is O(n)
            in the loop the max part is O(k)
        So together it is O(nk) not linear
        if k ~ n it is almost O(n^2)
        """
        if not nums:
            return []
        return [max(nums[i:i + k]) for i in range(len(nums) - k + 1)]
