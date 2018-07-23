class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        num_freq = dict()
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1

        for num in num_freq:
            if num_freq[num] > n // 2:
                return num
        return None