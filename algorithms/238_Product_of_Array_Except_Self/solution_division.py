class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_zeros = len([num for num in nums if num == 0])
        if num_zeros > 1:
            return [0] * len(nums)
        product = 1
        for num in nums:
            if num != 0:
                product *= num
        if num_zeros == 1:
            return [product if num == 0 else 0 for num in nums]
        return [product // num for num in nums]