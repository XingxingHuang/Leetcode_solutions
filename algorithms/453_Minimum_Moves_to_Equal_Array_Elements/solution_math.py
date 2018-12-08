class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # note there is no situation where you want hold the current minimal value unchanged and make all others plus 1
        # which means if the minimum number moves is k, then to get to the final result, the minimal value from the
        # begining must be added 1 for exactly k times
        # thus we have Eq: k*(len(nums)-1) + sum(nums) = len(nums) * (min(nums) + k)
        # solve for k gives the below:
        return sum(nums) - len(nums) * min(nums)
