# https://leetcode.com/problems/flipping-an-image/description/


class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        list comprehension and slicing
        """
        return [[e^1 for e in row[::-1]] for row in A]
