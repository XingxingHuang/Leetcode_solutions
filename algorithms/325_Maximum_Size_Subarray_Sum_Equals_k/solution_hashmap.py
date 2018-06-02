# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description/

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        # should be one pass with hashmap lookups
        1.
        utilize the fact that sub-arrays are always continues part of the array
        sum(nums[2:5]) can be calculated as sum(nums[:5]) - sum(nums[:2])
        so we don't need to loop over the array twice to get all sum(nums[a:b])
        but instead calculate them from sum(nums[:i]) that stored in lookups
        2.
        if we have sum(nums[:i1]) == sum(nums[:i2]) we only need to remember the location min(i1, i2)
        since if we figure out that sum(nums[i:g]) == k, we want max(g-i1, g-i2)
        """
        consecutive_sums = {}
        current_sum = 0
        max_length = 0
        for idx, num in enumerate(nums):
            current_sum += num
            if current_sum == k:
                max_length = idx + 1
            elif current_sum - k in consecutive_sums:
                max_length = max(max_length, idx - consecutive_sums[current_sum - k])
            if current_sum not in consecutive_sums:
                consecutive_sums[current_sum] = idx
        return max_length