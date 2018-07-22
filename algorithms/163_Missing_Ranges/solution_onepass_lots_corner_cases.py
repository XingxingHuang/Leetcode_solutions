class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        assert lower <= upper, 'lower is larger than upper'

        if not nums:
            if lower < upper:
                return ['{}->{}'.format(lower, upper)]
            else:
                return ['{}'.format(lower)]

        missing_ranges = []

        if lower < nums[0] - 1:
            missing_ranges.append('{}->{}'.format(lower, nums[0] - 1))
        elif lower == nums[0] - 1:
            missing_ranges.append('{}'.format(lower))

        for i, num in enumerate(nums[1:], 1):
            if num == nums[i - 1] + 2:
                missing_ranges.append('{}'.format(num - 1))
            elif num > nums[i - 1] + 2:
                missing_ranges.append('{}->{}'.format(nums[i - 1] + 1, num - 1))

        if nums[-1] + 1 < upper:
            missing_ranges.append('{}->{}'.format(nums[-1] + 1, upper))
        elif nums[-1] + 1 == upper:
            missing_ranges.append('{}'.format(upper))

        return missing_ranges
