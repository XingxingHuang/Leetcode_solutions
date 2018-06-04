class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        if number of stairs == 0 or 1, only 1 way of climbing
        if number of stairs > 1, counting from top to button
        the number of ways to get to n is the sum of number of ways to get to n-1 and number of ways to get to n - 2
        thus found a recursive pattern
        num(n) = num(n-1) + num(n-2)
        """
        if n == 0 or n == 1:
            return 1
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)
