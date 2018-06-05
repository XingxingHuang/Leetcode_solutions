# https://leetcode.com/problems/sliding-window-maximum/description/

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        [1 2 3] 4 4 3 7 idx = N, current_max = 3, max_nums = [3]
        1 [2 3 4] 4 3 7 idx = 4, current_max = 4, max_nums = [3 4]      nums[idx - k] = 2
        1 2 [3 4 4] 3 7 idx = 5, current_max = 4, max_nums = [3 4 4]    nums[idx - k] = 3
        1 2 3 [4 4 3] 7 idx = 6, current_max = 4, max_nums = [3 4 4 4]  nums[idx - k] = 4
        """
        if not nums:
            return []
        current_max = max(nums[:k])
        max_nums = [current_max]
        for idx, num in enumerate(nums[k:], start=k):
            if nums[idx] > current_max:
                current_max = nums[idx]
                max_nums.append(current_max)
            elif current_max != nums[idx - k]:   # the element that is leaving the window:
                max_nums.append(current_max)
            else:   # it is possible that the maximum element in the window has left
                current_max = max(nums[idx - k + 1: idx + 1]) # recalculating the max in the new window
                max_nums.append(current_max)
        return max_nums