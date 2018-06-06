
# [1,2,3,4] => sum = 4*(4 + 1) / 2 = 10
# [1,2,2,4] => sum = 9
# find duplicate value using set look ups => 2
# corrupted value is 2 + (10 - 9)


class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        act_total= sum(nums)
        idea_total = int(len(nums) * (len(nums) + 1) / 2)
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                break
        return [num, num + idea_total - act_total]