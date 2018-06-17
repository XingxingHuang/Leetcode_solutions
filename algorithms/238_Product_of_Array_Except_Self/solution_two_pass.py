class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = 1
        n = len(nums)
        results = []
        for num in nums:
            results.append(product)
            product *= num
        product = 1
        for idx, num in enumerate(nums[::-1]):
            results[n - idx - 1] *= product
            product *= num
        return results
