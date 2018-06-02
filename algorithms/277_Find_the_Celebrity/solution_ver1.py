#   https://leetcode.com/problems/find-the-celebrity/description/

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):
class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        # brute force, time limit exceed
        """
        m = [[knows(i, j) for j in range(n)] for i in range(n)]
        print(m)
        for i in range(n):
            if sum(m[i]) == 1 and sum([m[k][i] for k in range(n)]) == n:
                return i
        return -1
