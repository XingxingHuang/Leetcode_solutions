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
        candidates = set(range(n))
        for i in range(n):
            for j in range(n):
                if knows(i, j) and i != j:
                    candidates.remove(i)
                    break
        for candidate in candidates:
            if all(knows(i, candidate) for i in range(n)):
                return candidate
        return -1
