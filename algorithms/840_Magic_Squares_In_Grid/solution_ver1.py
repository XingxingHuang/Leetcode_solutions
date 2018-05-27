def check_magic_square(m):
    if set(sum(m, [])) != set(range(1, 10)):
        return False
    if not all(map(lambda row: sum(row) == 15, m)):
        return False
    if not all(map(lambda col: sum(col) == 15, zip(*m))):
        return False
    if not all(map(lambda diag: sum(diag) == 15, [[m[i][i] for i in range(3)], [m[i][2 - i] for i in range(3)]])):
        return False
    return True


class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        counts = 0
        for row_idx in range(len(grid) - 2):
            for col_idx in range(len(grid[0]) - 2):
                m = [row[col_idx:col_idx + 3] for row in grid[row_idx:row_idx + 3]]
                if check_magic_square(m):
                    counts += 1
        return counts
