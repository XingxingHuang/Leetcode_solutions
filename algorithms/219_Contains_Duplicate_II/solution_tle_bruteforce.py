class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        if k >= n:
            return len(set(nums)) < n

        for idx, num in enumerate(nums):
            if idx + k > n + 1:
                return False
            if num in nums[idx + 1: idx + 1 + k]:
                return True
        return False