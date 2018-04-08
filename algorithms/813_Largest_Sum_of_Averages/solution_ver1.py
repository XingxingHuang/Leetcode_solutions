# https://leetcode.com/problems/largest-sum-of-averages/description/

TAGS = ['DP']

class Solution:
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        N = len(A)
        cumsum = [0] + [sum(A[:i + 1]) for i in range(N)]
        slice_average = lambda x: (cumsum[x[1]] - cumsum[x[0]])/(x[1]-x[0])
        dp = [slice_average([i, N]) for i in range(N)]
        for k in range(K-1):
            for i in range(N):
                for j in range(i+1, N):
                    dp[i] = max(dp[i], slice_average([i, j]) + dp[j])

        return dp[0]