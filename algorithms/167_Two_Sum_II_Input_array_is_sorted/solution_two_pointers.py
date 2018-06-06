# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        small, large = 0, len(numbers)-1
        while small < large:
            total = numbers[small] + numbers[large]
            if total == target:
                return [small + 1, large + 1]
            if total > target:
                large -= 1
            else:
                small += 1
        return [-1, -1]