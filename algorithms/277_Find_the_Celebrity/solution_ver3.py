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
        # the reduce part find out a candidate celebrity
        # if i knows j      -> i is not a celebrity, j is a candidate
        # if i don't know j -> j is not a celebrity, i is still the candidate
        # ran a final scan to make sure
        """
        x = reduce(lambda i, j: j if knows(i, j) else i, range(n))
        return x if all(knows(i, x) and not knows(x, i) for i in range(n) if i != x) else -1
