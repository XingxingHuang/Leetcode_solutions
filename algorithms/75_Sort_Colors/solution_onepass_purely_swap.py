class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        end_0 = 0
        end_2 = n - 1
        curr = 0

        while curr <= end_2: # not n - 1
            if nums[curr] == 0:
                nums[end_0], nums[curr] = nums[curr], nums[end_0]
                end_0 += 1
            elif nums[curr] == 2:
                nums[end_2], nums[curr] = nums[curr], nums[end_2]
                end_2 -= 1
                curr -= 1 # don't forget this
            curr += 1

