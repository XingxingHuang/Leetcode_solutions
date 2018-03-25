class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_max = [max(row) for row in grid]
        col_max = [max(row) for row in zip(*grid)]
        opt = [[min(row_max[r], col_max[c]) for c in range(len(grid[0])) ] for r in range(len(grid)) ]
        return sum(sum(row) for row in opt) - sum(sum(row) for row in grid)