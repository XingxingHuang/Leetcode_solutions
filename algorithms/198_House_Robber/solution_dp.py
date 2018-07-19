class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = 0
        curr = 0
        for profit in nums:
            temp = curr
            curr = max(prev + profit, curr)
            prev = temp

        return curr