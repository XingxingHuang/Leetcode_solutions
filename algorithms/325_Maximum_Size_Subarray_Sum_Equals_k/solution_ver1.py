# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description/

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        # brute force, time exceeded
        """
        n = len(nums)
        length = 0
        for start in range(n):
            for end in range(start + 1, n + 1):
                new_length = end - start
                if new_length <= length:
                    continue
                elif sum(nums[start:end]) == k and new_length > length:
                    length = new_length
            if n - start <= length:
                break
        return length