class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        use a hashmap to store the maximum of sum of subarrarys ending at each location
        iterrativly build out this list
        the maximum number at a given location is either the current val or the sum of the current val and previous best
        """
        best_at_loc = [nums[0]] * len(nums)
        global_max = nums[0]
        for idx, num in enumerate(nums[1:], 1):
            best_at_loc[idx] = max(num, best_at_loc[idx - 1] + num)
            global_max = max(global_max, best_at_loc[idx])
        return global_max