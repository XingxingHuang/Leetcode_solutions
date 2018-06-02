# https://leetcode.com/problems/single-number/description/

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        # not good, using sort makes it n*log(n)
        """
        if len(nums) == 1:
            return nums[0]
        nums = sorted(nums)
        for idx, num in enumerate(nums):
            if idx == 0 and num != nums[idx + 1]:
                return num
            elif idx == len(nums) - 1 and num != nums[-2]:
                return num
            elif num != nums[idx -1] and num != nums[idx + 1]:
                return num