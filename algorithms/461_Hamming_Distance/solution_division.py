class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        d = 0
        while x or y:
            d += x % 2 != y % 2
            x =  x // 2
            y = y // 2
        return d