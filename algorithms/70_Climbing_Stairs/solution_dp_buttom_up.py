class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        # watch out the upper boundary in the loop
        """
        if n == 0 or n == 1:
            return 1
        ways = [1,1]
        for i in range(2, n + 1):
            ways.append(ways[i - 1] + ways[i - 2])
        return ways[-1]


