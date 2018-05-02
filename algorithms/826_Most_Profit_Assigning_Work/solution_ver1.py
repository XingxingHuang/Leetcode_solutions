# https://leetcode.com/problems/most-profit-assigning-work/description/

class Solution():
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        dp = list(zip(difficulty, profit))
        dp.sort()
        worker.sort()
        total = 0
        best_profit = 0
        i = 0
        for s in worker:
            while i < len(dp) and s >= dp[i][0]:
                best_profit = max(best_profit, dp[i][1])
                i += 1
            total += best_profit
        return total

