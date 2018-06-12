# https://leetcode.com/problems/two-sum/description/
TAGS = ['ARRAY', 'HASHMAP']


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        it is crucial to check before insert, this avoids 4 = 2 + 2 when it first encounter 2
        """
        num_index_map = {}
        for idx, num in enumerate(nums):
            if target - num in num_index_map:
                return [idx, num_index_map[target - num]]
            num_index_map[num] = idx