#  https://leetcode.com/problems/find-the-duplicate-number/solution/


class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        # time O(n) iterate over 4 times
        # space O(n) for set
        """
        return int((sum(nums) - sum(set(nums))) / (len(nums) - len(set(nums))))