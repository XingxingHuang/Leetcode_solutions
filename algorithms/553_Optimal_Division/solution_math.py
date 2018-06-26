class Solution:
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        consider three number cases a, b, c
        only two options:
        a/(b/c) or a/b/c
        and since the elements are all >=2
        a/(b/c) = c*a/b is definitly bigger than a/b/c
        so max(a,b,c) = a/(b/c)  min(a,b,c) = a/b/c
        for more number cases
        nums[0], nums[1], nums[2], ...
        max0 = nums[0] / (min(nums[1:]))
        min1 = nums[1]/ (max[nums[2:]])
        etc
        recursive?
        wait. the min(nums[1:]) should be nums[1]/nums[2]/nums[3]/...
        since if there is a bracket in them, it is equvalent to filp a number to the numerator and multiply with nums[1]!
        """
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return "{}/{}".format(nums[0], nums[1])
        result = "{}/({}".format(nums[0], nums[1])
        for num in nums[2:]:
            result += '/{}'.format(num)
        result += ')'
        return result
