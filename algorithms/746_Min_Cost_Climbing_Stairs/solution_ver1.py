# https://leetcode.com/problems/min-cost-climbing-stairs/description/


class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) == 0:
            return 0
        if len(cost) <= 2:
            return cost[0]
        current_cost = 0
        path_1 = cost[0]
        path_2 = cost[1]
        for c in cost[2:]:
            path_1, path_2 = path_2, min(path_1, path_2) + c
        return min(path_1, path_2)