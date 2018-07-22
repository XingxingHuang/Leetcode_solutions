class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        nrows = len(matrix)  # m
        ncols = len(matrix[0])  # n
        zero_cols = set()
        zero_rows = set()

        # O(m*n)
        for r in range(nrows):
            for c in range(ncols):
                if matrix[r][c] == 0:
                    zero_cols.add(c)
                    zero_rows.add(r)

        for r in zero_rows:
            for c in range(ncols):
                matrix[r][c] = 0

        for c in zero_cols:
            for r in range(nrows):
                matrix[r][c] = 0
