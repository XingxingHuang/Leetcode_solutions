# https://leetcode.com/problems/soup-servings/description/


class Solution:
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        The probability is monotonically increasing as N increases.
        When N >= 5600, the probability is within 10^-6 to 1
        When N is smaller, use dp
        """
        if N >= 5600:
            return 1

        memo = {}
        def dp(x, y):
            if (x, y) not in memo:
                if x <= 0 and y <= 0:
                    ans = 0.5
                if x <= 0 and y > 0:
                    ans = 1
                if x > 0 and y <= 0:
                    ans = 0
                if x > 0 and y > 0:
                    ans = 0.25 * (dp(x - 100, y) + dp(x - 75, y - 25) +
                                  dp(x - 50, y - 50) + dp(x - 25, y - 75))
                memo[x, y] = ans
            return memo[x, y]

        return dp(N, N)