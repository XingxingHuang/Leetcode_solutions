class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        nr, nc = len(M), len(M[0])
        A = [[0 for _ in range(nc)] for _ in range(nr)]
        for r in range(nr):
            for c in range(nc):
                count = 0
                total = 0
                for sr in [r - 1, r, r + 1]:
                    for sc in [c - 1, c, c + 1]:
                        if 0 <= sr < nr and 0 <= sc < nc:
                            count += 1
                            total += M[sr][sc]
                A[r][c] = int(total / count)
        return A