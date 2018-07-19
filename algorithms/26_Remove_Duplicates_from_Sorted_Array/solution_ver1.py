class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = 0
        for i in range(1, len(nums)):
            if nums[pos] != nums[pos+1]:
                pos += 1
            else:
                del nums[pos]
        return len(nums)
