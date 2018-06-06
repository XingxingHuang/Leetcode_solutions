class Solution():
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self._out = []
        self._backtracking([], nums, len(nums))
        return self._out

    def _backtracking(self, perms, nums, length):
        if len(perms) == length:
            self._out.append(perms[:])  ## crucial!!!!!
        for idx, num in enumerate(nums):
            perms.append(num)
            self._backtracking(perms, nums[:idx] + nums[idx + 1:], length)
            perms.pop()