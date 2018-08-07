# https://leetcode.com/problems/unique-paths/description/

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        M = [[0 for _ in range(m)] for _ in range(n)]
        M[0][0] = 1
        # print(M)
        for r in range(n):
            for c in range(m):
                if r == 0 and c == 0:
                    continue
                elif r == 0 and c > 0:
                    M[r][c] = M[r][c - 1]
                elif c == 0 and r > 0:
                    M[r][c] = M[r - 1][c]
                else:
                    M[r][c] = M[r - 1][c] + M[r][c - 1]
                # print(r, c, M)
        return M[n-1][m-1]