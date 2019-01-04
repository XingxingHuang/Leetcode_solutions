class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        for l, lh in enumerate(height[:-1]):
            for r, rh in enumerate(height[l+1:], l + 1):
                max_area = max(max_area, min(lh, rh) * (r-l))
        return max_area

