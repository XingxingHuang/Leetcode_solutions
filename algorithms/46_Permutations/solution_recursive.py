class Solution():
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out = []
        if len(nums) == 1:
            out = [nums]
        else:
            for idx, num in enumerate(nums):
                for perm in self.permute(nums[:idx] + nums[idx+1:]):
                    out.append([num] + perm)
        return out