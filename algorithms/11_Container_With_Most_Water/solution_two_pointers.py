class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
	# start from both ends, iterativly move the shorter one towards the 
        # longer one
        l, r, lh, rh = 0, len(height) - 1, height[0], height[-1]
        max_area = min(lh, rh) * (r - l)
        while l != r:
            if lh <= rh:
                l += 1
                lh = height[l]
            else:
                r -= 1
                rh = height[r]
            max_area = max(max_area, min(lh, rh) * (r - l))

        return max_area
