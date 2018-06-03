# https://leetcode.com/problems/rotate-image/description/

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        I don't think this is inplace
        """
        matrix[:] = list(map(list, zip(*matrix[::-1])))

