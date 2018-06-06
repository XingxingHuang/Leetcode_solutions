class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = two = three = -float('inf')
        for num in nums:
            if num > one:
                one, two, three = num, one, two
            elif one > num > two: # this is neccessary
                two, three = num, two
            elif two > num > three: # this is neccessary too!
                three = num
        return three if three != -float('inf') else one