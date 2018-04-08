# https://leetcode.com/problems/largest-triangle-area/description/
TAGS = ['MATH']


class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        brute force solution using formula:
        area = 1/2 * abs(ax * (by-cy) + bx * (cy-ay) + cx * (ay-by))
        """
        from itertools import combinations
        return max([abs(a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (
                    a[1] - b[1])) / 2 for a, b, c in combinations(points, 3)])
