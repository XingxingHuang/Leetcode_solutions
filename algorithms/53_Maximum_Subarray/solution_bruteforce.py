class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        brute force double loop, time limit exceed
        """
        if len(nums) == 1:
            return nums[0]
        max_sum = -float('inf')
        for start in range(len(nums)):
            for end in range(start + 1, len(nums) + 1):
                # print(start, end)
                current_sum = sum(nums[start:end])
                max_sum = max(current_sum, max_sum)
        return max_sum
