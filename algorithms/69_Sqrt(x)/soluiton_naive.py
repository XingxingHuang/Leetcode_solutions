class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 1
        while i**2 < x:
            i += 1
        return i if i**2 == x else i - 1