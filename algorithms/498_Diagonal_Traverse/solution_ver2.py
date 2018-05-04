# https://leetcode.com/problems/diagonal-traverse/description/

class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        for matrix of shape [3, 3] the correct order of indices are:
        [0,0] > [0,1], [1,0] < [2,0], [1,1], [0,2] > [1,2], [2,1] < [2,2]
        by j           by i              by j           by i         by j
        > , < indicates a traversal direction change
        notice sum of [i, j] remain same along before a direction change

        idea is to generate the correct ordered list of [i, j] pairs
        sort by sum(i, j) first then by i or by j based on direction
        bit wise operation 1 with sum of m[i][j] gives the direction


        """
        if matrix == []:
            return []
        m, n = len(matrix), len(matrix[0])
        indices = [(i,j) for i in range(m) for j in range(n)]
        indices.sort(
            key=lambda x: (
                sum(x),
                (x[1], x[0])[sum(x) & 1]
            ))
        return [matrix[i][j] for [i, j] in indices]


