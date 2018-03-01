# https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/


class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # this is linear solution, slightly faster than the one using sorting
        largest, second_largest = -1, -1
        index = 0
        for idx, num in enumerate(nums):
            if num > largest:
                second_largest = largest
                largest = num
                index = idx
            elif num > second_largest:
                second_largest = num
        return index if largest >= 2* second_largest else -1