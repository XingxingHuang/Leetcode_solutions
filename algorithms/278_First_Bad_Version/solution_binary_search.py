# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.binary_search(low=1, high=n)

    def binary_search(self, low, high):

        mid = (low + high) // 2

        if isBadVersion(mid):
            if not isBadVersion(mid - 1):
                return mid

        return self.binary_search(low, mid)

        else:
        return self.binary_search(mid + 1, high)