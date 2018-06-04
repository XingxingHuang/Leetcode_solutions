class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        # watch out the upper boundary in the loop
        """
        current, prev = 1, 1
        for _ in range(1, n):
            current, prev = current + prev, current
        return current

