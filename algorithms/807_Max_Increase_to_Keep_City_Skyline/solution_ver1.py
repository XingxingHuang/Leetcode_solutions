# https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/

class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        this is a math problem, the optimal value per cell[i,j] is the min of the two maximums in row and column
        """
        row_max = [max(row) for row in grid]
        col_max = [max(row) for row in zip(*grid)]
        opt = [[min(row_max[r], col_max[c]) for c in range(len(grid[0])) ] for r in range(len(grid)) ]
        return sum(sum(row) for row in opt) - sum(sum(row) for row in grid)