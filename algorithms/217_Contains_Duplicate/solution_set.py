class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_scanned = set()
        for num in nums:
            if num not in num_scanned:
                num_scanned.add(num)
            else:
                return True
        return False
        # below is faster, but might not be good in interview
        # return len(set(nums)) < len(nums)