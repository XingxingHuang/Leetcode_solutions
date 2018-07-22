class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums.sort()
        for e in nums:
            res += [l+[e] for l in res]
        return res