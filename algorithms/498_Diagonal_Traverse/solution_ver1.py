# https://leetcode.com/problems/diagonal-traverse/description/

class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        bruteforce, solve it as described...
        """
        if matrix == []:
            return []
        i, j = 0, 0
        m, n = len(matrix) - 1, len(matrix[0]) - 1
        move_upperright = True
        results = [matrix[i][j]]
        while (i, j) != (m, n):
            if move_upperright:
                if i == 0 and j != n:  # reaching top but not top right
                    j += 1
                    move_upperright = False
                elif j == n:  # reaching right
                    i += 1
                    move_upperright = False
                else:
                    j += 1
                    i -= 1
            else:
                if j == 0 and i != m:  # reaching left but not bottom:
                    i += 1
                    move_upperright = True
                elif i == m:  # reach bottom
                    j += 1
                    move_upperright = True
                else:
                    i += 1
                    j -= 1
            results.append(matrix[i][j])
        return results



